# Scientific discovery in the age of artificial intelligence

> **저자**: Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal Chandak, Shengchao Liu, Peter Van Katwyk, Andreea Deac, Anima Anandkumar, Karianne Bergen, Carla P. Gomes, Shirley Ho, Pushmeet Kohli, Joan Lasenby, Jure Leskovec, Tie-Yan Liu, Arjun Manrai, Debora Marks, Bharath Ramsundar, Le Song, Jimeng Sun, Jian Tang, Petar Velickovic, Max Welling, Linfeng Zhang, Connor W. Coley, Yoshua Bengio, Marinka Zitnik | **날짜**: 2023 | **Journal**: Nature | **DOI**: 10.1038/s41586-023-06221-2

---

## Essence

AI가 과학 발견의 전 과정 -- 가설 생성, 실험 설계, 데이터 수집/해석 -- 을 어떻게 augment하고 가속하는지를 체계적으로 정리한 종합 리뷰이다. Self-supervised learning, geometric deep learning, generative AI, reinforcement learning 등 핵심 기법이 물리학, 화학, 생물학, 지구과학 등 다양한 분야에서 과학적 발견을 가능하게 하는 방식을 분석하고, 데이터 품질, out-of-distribution 일반화, 해석 가능성 등 남은 과제를 제시한다.

## Motivation

- **알려진 것**: 2010년대 초 deep learning의 부상 이후 AI가 과학 연구에 점점 더 통합되고 있으며, AlphaFold의 protein folding 문제 해결 등 획기적 성과가 나타남
- **Gap**: AI4Science 분야의 급속한 발전에도 불구하고, 다양한 과학 분야에 걸친 AI 방법론의 체계적 정리가 부족하고, 실용적 한계와 미래 방향에 대한 통합적 시각이 필요
- **왜 중요한가**: AI가 과학 발견의 패러다임을 근본적으로 변화시키고 있으나, 개발자와 사용자 모두 이 접근법의 개선 필요 시점과 데이터 품질/관리 문제를 이해해야 함
- **접근법**: 과학적 발견 프로세스의 각 단계(데이터 수집, 표현 학습, 가설 생성, 실험/시뮬레이션)를 중심으로 AI 기법의 적용 사례와 과제를 분류 정리

## Achievement

1. **과학 발견 프로세스의 체계적 AI 매핑**: 데이터 수집(selection, annotation, generation, refinement) -> 표현 학습 -> 가설 생성 -> 실험/시뮬레이션의 전 과정을 AI 관점에서 구조화
2. **핵심 AI 기법의 과학적 적용 사례 정리**: Geometric deep learning (분자 구조, GNN), self-supervised learning (protein language model, contrastive learning), generative models (VAE, GAN, diffusion, normalizing flows), reinforcement learning (tokamak 제어, 합성 경로 탐색)
3. **분야 횡단적 연결 제시**: 입자 물리학의 rare event detection, 생물학의 protein folding, 화학의 synthesis planning, 천체물리학의 gravitational wave 분석 등을 통합적 프레임워크로 연결
4. **Grand challenges 식별**: Out-of-distribution 일반화, multimodal 데이터 통합, 과학 지식의 inductive bias 통합, 해석 가능성, causality 등 5대 핵심 과제 도출
5. **과학 기업 생태계 변화 전망**: 연구팀 구성의 변화, 산학 협력 모델, self-driving lab, 교육 프로그램 등 AI4Science의 사회적 영향 논의

## How

- **구조**: 과학적 발견의 4단계 (관찰-가설-실험-이론)를 중심으로 AI 기법을 매핑하는 narrative review
- **범위**: 238개 참고문헌을 통해 물리학, 화학, 생물학, 지구과학, 수학, 의학 등 광범위한 분야를 커버
- **핵심 프레임워크**:
  - Data collection: anomaly detection (autoencoder), pseudo-labelling, active learning, data augmentation (GAN)
  - Representation learning: geometric deep learning (GNN, equivariance), self-supervised learning (contrastive, masked-language modelling), transformer, neural operator
  - Hypothesis generation: black-box predictor (high-throughput screening), symbolic regression (RL), differentiable hypothesis space (VAE + Bayesian optimization), GFlowNet
  - Experimentation/simulation: RL for experiment steering (tokamak plasma control), neural potential (molecular dynamics), physics-informed neural networks (PDE solver), normalizing flows (Boltzmann generator)

## Originality

- **통합적 프레임워크**: 개별 분야에서 독립적으로 발전해온 AI4Science 연구를 과학적 발견 프로세스라는 단일 프레임워크 하에 최초로 체계적 통합
- **분야 횡단적 알고리즘 연결**: 입자 물리학의 anomaly detection과 생물학의 cell type discovery, 화학의 molecular design과 수학의 symbolic regression 등 서로 다른 분야에서 공통 알고리즘이 적용되는 패턴을 명확히 식별
- **Grand challenges의 구체화**: Out-of-distribution 일반화 문제를 causality와 연결하고, multimodal 데이터 통합과 해석 가능성을 과학적 맥락에서 구체적으로 정의

## Limitation & Further Study

### 저자들이 언급한 한계

- 과학 데이터의 불완전성, 편향, 접근성 제한 (privacy, safety)으로 AI 분석에 직접 적용 어려움
- Out-of-distribution 일반화가 AI 연구의 최전선 과제이며, 현재 transfer learning 체계는 ad hoc하고 이론적 가이드 부족
- Black-box 모델의 해석 가능성이 부족하여 정책 결정이나 고위험 영역에서의 신뢰성 문제
- AI 도구의 오용 및 dual use 위험 (예: 약물 설계 알고리즘의 화학무기 전용 가능성)
- 모델의 재현성 문제 -- stochastic training, 변동하는 데이터셋, 구현 차이

### 자체판단 아쉬운 점

- Review 논문의 특성상 개별 기법의 기술적 깊이가 제한적이며, 각 분야 전문가에게는 surface-level 정리에 그칠 수 있음
- LLM (GPT 계열)의 과학 발견 적용에 대한 논의가 상대적으로 부족 -- 2023년 출판 시점 이후 급격히 발전한 영역
- 실제 과학 발견으로 이어진 AI 기반 성공 사례의 정량적 분석 (성공률, 비용 절감, 시간 단축 등)이 부족
- 분야별 AI 도입 성숙도의 차이에 대한 분석이 피상적

### 후속 연구

- Foundation model의 과학 분야별 적용 전략 및 domain adaptation 방법론 체계화
- Causal inference와 deep learning의 통합을 통한 out-of-distribution 일반화 개선
- Self-driving lab과 AI agent의 autonomous discovery 능력 실증 연구
- Multimodal scientific data의 통합 표현 학습 프레임워크 개발
- AI4Science 교육 커리큘럼 및 인력 양성 체계 구축

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 3/5 |
| Technical Soundness | 4/5 |
| Significance | 5/5 |
| Clarity | 5/5 |
| Overall | 4/5 |

**총평**: AI4Science 분야의 landscape를 가장 포괄적으로 조망한 리뷰로, 과학 발견 프로세스 전반에 걸친 AI 기법의 체계적 정리와 grand challenges 식별이 뛰어나다. 다만 review 논문 특성상 기술적 novelty는 제한적이며, LLM 시대의 급변하는 상황을 완전히 반영하지 못한 한계가 있다.
