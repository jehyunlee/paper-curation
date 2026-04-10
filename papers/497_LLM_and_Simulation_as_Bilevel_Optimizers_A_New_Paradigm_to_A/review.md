---
title: "497_LLM_and_Simulation_as_Bilevel_Optimizers_A_New_Paradigm_to_A"
authors:
  - "Pingchuan Ma"
  - "Tsun-Hsuan Wang"
  - "Minghao Guo"
  - "Zhiqing Sun"
  - "J. B. Tenenbaum"
date: "2024"
doi: "10.48550/arXiv.2405.09783"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(LLM)의 추론 능력과 물리 시뮬레이션의 계산 정확성을 결합한 **이단계 최적화 프레임워크(bilevel optimization)**를 제안하여, 물리 과학 발견(구성법칙 발견, 분자 설계)에서 인간 기대를 초월한 새로운 해를 찾을 수 있음을 보여준다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/AI-Powered_Research_Planning"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Ma et al._2024_LLM and Simulation as Bilevel Optimizers A New Paradigm to Advance Physical Scientific Discovery.pdf"
---

# LLM and Simulation as Bilevel Optimizers: A New Paradigm to Advance Physical Scientific Discovery

> **저자**: Pingchuan Ma, Tsun-Hsuan Wang, Minghao Guo, Zhiqing Sun, J. B. Tenenbaum | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2405.09783](https://doi.org/10.48550/arXiv.2405.09783)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: Scientific Generative Agent (SGA)의 전체 파이프라인. 순수 탄성 재료로부터 약한 압축성 유체로 최적화되는 구성법칙 탐색 문제를 예시로 보여줌.*

본 논문은 대규모 언어모델(LLM)의 추론 능력과 물리 시뮬레이션의 계산 정확성을 결합한 **이단계 최적화 프레임워크(bilevel optimization)**를 제안하여, 물리 과학 발견(구성법칙 발견, 분자 설계)에서 인간 기대를 초월한 새로운 해를 찾을 수 있음을 보여준다.

## Motivation

- **Known**: LLM은 광범위한 지식과 고급 추론 능력으로 과학 발견에서 주목받고 있으며, 물리 시뮬레이션은 수치 정확성과 미분가능성을 제공함
  
- **Gap**: LLM 단독으로는 관찰 피드백(observational feedback) 시뮬레이션 능력이 부족하고, 시뮬레이션 단독으로는 이산적(discrete) 가설 생성 능력이 제한적임. 기존 연구는 특정 도메인에만 적용 가능한 문제 해결책만 제시함
  
- **Why**: 인간 과학자들은 (i) 가설을 반복적으로 제안하고 실험을 통해 관찰, (ii) 이산 요소(물리 방정식, 분자 구조)와 연속 요소(물리 파라미터)를 분리, (iii) 기존 지식을 활용하면서 혁신적 아이디어도 탐색하는 방식으로 과학 발견을 수행함
  
- **Approach**: LLM을 외부 수준(outer-level) 최적화에서 이산 공간의 가설 생성 모듈로, 미분가능 시뮬레이션을 내부 수준(inner-level) 최적화에서 연속 파라미터 정제 모듈로 활용하는 통합 프레임워크 제안

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 손실값(loss) 추이 비교. 최고 성능 솔루션의 손실값을 반복 횟수에 따라 표시.*

1. **구성법칙 발견(Constitutive Law Discovery)**: 운동 궤적만으로부터 복잡한 비선형 재료 구성 방정식을 자동 발견. 초기 선형 탄성 모델로부터 약한 압축성 유체(weakly compressible fluid) 표현까지 최적화되는 과정을 통해 손실값을 10.0에서 0.1로 감소

2. **분자 설계(Molecular Design)**: 분자 구조와 원자 좌표를 동시에 최적화하여 입자자 수준의 양자역학적 성질을 만족하는 분자 발견. 기존 휴리스틱 방법과 비교하여 우월한 성능 달성

3. **예상을 초월한 해의 발견**: 기존 인간 기대와 다르지만 도메인 전문가에 의해 합리적으로 검증되는 새로운 솔루션 제시

## How

![Figure 3](figures/fig3.webp)
*그림 3: 이단계 최적화에 대한 절제 실험(ablation study). 외부 최적화와 내부 최적화의 기여도 분석.*

![Figure 4](figures/fig4.webp)
*그림 4: 백본 LLM에 대한 절제 실험. 다양한 LLM 모델 간 성능 비교.*

- **형식적 정의**: 시뮬레이터 Φ(θ; E)가 과학적 표현식 E(물리 방정식 등)와 연속 파라미터 θ(재료 성질 등)를 입력받아 시뮬레이션 결과 y와 관찰 피드백 z를 산출

- **이단계 최적화 공식**:
  - 외부 최적화: min_{E,Θ} L(y(E, Θ, θ̂; Φ)) - LLM이 제약조건 G(E,Θ;Φ)≤0(시뮬레이션 유효성) 하에서 표현식 E와 파라미터화 전략 Θ 탐색
  - 내부 최적화: θ̂ ∈ argmin_{θ∈Θ} L(y(θ;Φ,E)) - 미분가능 시뮬레이션으로 주어진 E에 대해 최적 연속 파라미터 결정

- **LLM 기반 외부 최적화**:
  - Top-K 힙(heap) 데이터 구조로 우수 솔루션 관리
  - 과거 실험 결과 분석, 고수준 계획 수립, 실행 가능한 코드 스니펫 제안을 위한 체계적 프롬프팅
  - 진화적 탐색으로 각 반복에서 M개 자손 {E_m, Θ_m} 생성

- **탐색-활용(Explore-Exploit) 전략**: 
  - 활용(Exploit) 온도 T_l로 M_l개 솔루션 생성 → 상위 성능 솔루션 개선
  - 탐색(Explore) 온도 T_h로 M_h개 솔루션 생성 → 새로운 영역 탐색

- **시뮬레이션 인터페이싱**:
  - 방정식 탐색(Equation Searching): LLM이 물리 방정식 E와 최적화 공간 Θ 동시 제안
  - 엔티티 탐색(Entity Searching): 분자 구조 같은 구조화된 객체 최적화

## Originality

- **통합 프레임워크**: 이산 최적화(LLM 기반)와 연속 최적화(미분가능 시뮬레이션)를 명시적 이단계 최적화로 통합한 첫 시도. 기존 LLM 기반 과학 발견은 계산 정확성 부족 문제를 해결하지 못함

- **인간 과학 방법론 기반 설계**: 포퍼의 가설-검증 사이클, 이산-연속 성분 분리, 탐색-활용 균형이라는 인간 과학자의 실제 관행을 체계화

- **도메인 범용성**: 최소한의 프롬프트 수정만으로 구성법칙 발견, 분자 설계 등 다양한 물리 과학 분야에 적용 가능한 범용 방법론 제시

- **예상 초월적 발견**: 인간의 기존 지식과 다른 새로운 구성 모델 발견 및 이론적 타당성 검증으로 과학적 혁신의 가능성 증명

## Limitation & Further Study

- **시뮬레이션 미분가능성 요구**: 연속 최적화가 미분가능한 시뮬레이션에 의존하기 때문에 이산 시뮬레이션이나 불연속 물리 현상으로의 확장 제한

- **계산 비용 분석 부재**: 각 반복마다 시뮬레이션이 필요한 점에서 계산 복잡도와 실제 실행 시간에 대한 상세한 분석 필요

- **LLM 크기별 영향**: Figure 4에서 LLM 선택의 영향을 보이지만, 더 정교한 LLM의 한계(hallucination, 부정확한 코드 생성)에 대한 대처 방안 미흡

- **검증 범위**: 두 가지 응용 분야(구성법칙, 분자 설계)에만 검증. 생물학, 화학 공학 등 다양한 과학 분야로의 확대 검증 필요

- **프롬프트 엔지니어링의 영향**: 체계적인 프롬프트 설계의 중요성은 언급하나, 프롬프트 변화에 따른 수렴성 및 해의 품질 변동성 분석 부재

## Evaluation

- **Novelty**: 4.5/5
  - 이단계 최적화로 LLM과 시뮬레이션을 통합하는 개념은 신선함
  - 하지만 진화적 알고리즘과 미분 최적화의 조합 자체는 기술적으로 새로운 것은 아님

- **Technical Soundness**: 4/5
  - 이단계 최적화 공식화는 수학적으로 견고함
  - 내부 최적화의 수렴성 보장, 외부 최적화의 종료 조건 등 이론적 분석 필요

- **Significance**: 4/5
  - 물리 과학 발견의 자동화라는 중요한 문제 다룸
  - 실제 과학 연구에 즉시 적용 가능한 실용성 높음
  - 다만 현재는 상대적으로 단순한 문제(저차원 파라미터 공간)에만 검증됨

- **Clarity**: 3.5/5
  - 전체 파이프라인은 명확하게 설명됨
  - Algorithm 1의 구현 세부사항과 프롬프트 설계 과정에 대한 설명 부족
  - 수학 기호(특히 Θ, o_k)의 정의가 명확하지 않은 부분 있음

- **Overall**: 4/5

**총평**: 본 논문은 LLM의 추론 능력과 시뮬레이션의 계산 정확성을 이단계 최적화로 우아하게 결합하여 물리 과학 발견을 자동화하는 실질적이고 범용적인 프레임워크를 제시한 견고한 연구이다. 특히 기대를 초월한 새로운 과학적 해를 발견할 수 있음을 실증적으로 보여준 점이 의미 있지만, 이론적 수렴성 분석과 더 복잡한 문제로의 확장 검증이 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — 물리학 정보 기반 신경망을 통한 과학적 머신러닝은 LLM과 물리 시뮬레이션을 결합한 이단계 최적화의 이론적 기반이다.
- 🔗 후속 연구: [[papers/697_Scaling_physical_reasoning_with_the_physics_dataset/review]] — 물리적 추론을 위한 물리학 데이터셋 확장은 LLM과 시뮬레이션의 이단계 최적화를 더 광범위한 물리 현상으로 확장한다.
- 🧪 응용 사례: [[papers/619_Physics_Informed_Deep_Learning_Part_I_Data-driven_Solutions/review]] — 물리학 정보 기반 딥러닝의 데이터 중심 솔루션은 LLM과 시뮬레이션 결합의 구체적인 물리 문제 적용 사례다.
