---
title: "469_Large_Language_Models_as_Evolutionary_Optimizers"
authors:
  - "Shengcai Liu"
  - "Caishun Chen"
  - "Xinghua Qu"
  - "Ke Tang"
  - "Y. Ong"
date: "2023"
doi: "10.1109/CEC60901.2024.10611913"
arxiv: ""
score: 4.0
essence: "본 논문은 대규모 언어모델(Large Language Models, LLM)을 진화 알고리즘(Evolutionary Algorithms, EA)의 연산자로 활용하여 조합 최적화 문제를 해결하는 최초의 시도를 제시한다. LLM 기반 진화 알고리즘(LMEA)은 도메인 전문 지식 없이도 자연어 명령만으로 부모 선택, 교차(crossover), 돌연변이(mutation) 연산을 수행할 수 있다."
tags:
  - "cat/AI-Powered_Scientific_Research_Frameworks"
  - "sub/Scientific_Agent_Frameworks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Liu et al._2023_Large Language Models as Evolutionary Optimizers.pdf"
---

# Large Language Models as Evolutionary Optimizers

> **저자**: Shengcai Liu, Caishun Chen, Xinghua Qu, Ke Tang, Y. Ong | **날짜**: 2023 | **DOI**: [10.1109/CEC60901.2024.10611913](https://doi.org/10.1109/CEC60901.2024.10611913)

---

## Essence

본 논문은 대규모 언어모델(Large Language Models, LLM)을 진화 알고리즘(Evolutionary Algorithms, EA)의 연산자로 활용하여 조합 최적화 문제를 해결하는 최초의 시도를 제시한다. LLM 기반 진화 알고리즘(LMEA)은 도메인 전문 지식 없이도 자연어 명령만으로 부모 선택, 교차(crossover), 돌연변이(mutation) 연산을 수행할 수 있다.

## Motivation

- **Known**: 진화 알고리즘은 복잡한 조합 최적화 문제 해결에 성공적이지만, 높은 성능을 위해서는 도메인 전문가가 문제 구조를 분석하여 맞춤형 유전 연산자를 설계해야 함. 최근 메타 최적화 패러다임은 알고리즘 설계 자동화를 시도하나 방대한 계산 자원과 대표성 있는 훈련 세트 선정의 어려움이 존재.

- **Gap**: LLM의 강력한 추론 및 의사결정 능력이 최적화 문제 해결에 직접 활용된 사례는 거의 없음. 특히 LLM을 진화 알고리즘의 핵심 연산자로 통합하는 연구가 부재.

- **Why**: LLM은 방대한 텍스트 데이터로부터 학습한 인간의 지식과 직관을 내포하고 있으므로, 알고리즘 설계의 경험과 휴리스틱도 포함하고 있을 가능성이 높음.

- **Approach**: 자연어 프롬프트를 통해 LLM에게 부모 선택과 유전 연산을 지시하고, LLM의 온도(temperature) 파라미터를 자동 조절하여 탐색(exploration)과 활용(exploitation)의 균형을 유지하는 LMEA 프레임워크 제안.

## Achievement

![Figure 1](figures/fig1.webp) *LMEA의 개요 및 프롬프트 구성 예시*

1. **경쟁력 있는 성능**: LMEA는 20개 노드 규모의 TSP(Traveling Salesman Problem) 인스턴스에서 전통적 휴리스틱과 견줄 만한 성능을 달성하며, 특히 10개 및 15개 노드 규모에서는 최적해를 일관되게 발견.

2. **최소한의 설계 노력**: 추가 모델 훈련이나 광범위한 도메인 전문 지식 없이 자연어 프롬프트 변경만으로 다양한 최적화 문제에 적응 가능.

3. **자동 적응 메커니즘의 효과성**: 온도 자동 조절 메커니즘이 지역 최적해 함정을 회피하고 탐색 성능을 향상시킴을 실증.

## How

![Figure 2](figures/fig2.webp) *LMEA와 OPRO의 세대 수에 따른 수렴 곡선 비교*

- **프롬프트 설계**: 과제 설명(task description), 해의 속성(solution properties), 집단 정보(population information), 연산자 지시(operator instructions)를 포함하는 구조화된 다중 파트 프롬프트 구성. 체인-오브-씽크(Chain-of-Thought) 기법 활용.

- **알고리즘 프레임워크**: 
  - 초기 집단 무작위 생성
  - 각 세대에서 LLM에 프롬프트 전달
  - N개 자손 해 생성
  - 현재 집단과 자손 중 상위 N개 해 선택
  - 온도 파라미터 자동 조절

- **온도 자동 조절**: 수렴 정체 감지 시 LLM의 온도를 증가시켜 다양성 증대, 진행 상황 감시 시 감소시켜 활용 강화.

- **Zero-shot 활용**: 사전 훈련된 LLM을 추가 미세조정(fine-tuning) 없이 즉시 사용하여 계산 자원 절감.

## Originality

- **LLM을 진화 알고리즘의 핵심 연산자로 직접 통합한 최초 연구**: 기존 연구는 LLM을 신경망 구조 생성이나 프롬프트 진화에 활용했으나, 진화 최적화의 부모 선택, 교차, 돌연변이 연산자로 사용한 사례는 없음.

- **새로운 알고리즘 설계 패러다임**: 형식적 문제 정의와 프로그래밍 대신 자연어 기반의 직관적 명령으로 알고리즘 구성. 메타 최적화와 달리 추가 훈련 불필요.

- **자적응 메커니즘의 통합**: LLM의 온도 파라미터를 진화 과정 중 동적으로 조절하여 탐색-활용 균형 자동화.

## Limitation & Further Study

- **제한된 문제 영역**: TSP만을 대상으로 실험하였으며, 최대 20개 노드 규모의 소규모 인스턴스에서만 검증. 현실적 대규모 조합 최적화 문제(수천 개 노드 이상)로의 확장 가능성 불명확.

- **성능 상한**: 본 연구의 목표가 최신 전문화된 TSP 솔버를 능가하는 것이 아니며, 여전히 고도로 최적화된 휴리스틱에 비해 성능이 낮을 가능성 높음.

- **프롬프트 엔지니어링의 의존성**: 효과적인 프롬프트 설계가 성능에 중대한 영향을 미치나, 최적 프롬프트 자동 탐색 방법론 부재.

- **LLM 토큰 비용**: 각 세대마다 LLM 쿼리 필요로 인한 높은 계산 비용(API 호출 비용 포함).

- **후속 연구 방향**:
  - 제약 조건이 있는 조합 최적화 문제(VRP, JSSP 등)로 확장
  - 프롬프트 최적화 자동화 기법 개발
  - 다목적 최적화 문제로의 응용
  - 매우 큰 규모 인스턴스에서의 확장성 개선
  - LLM 제약(토큰 길이 제한) 극복 방안 연구

## Evaluation

- **Novelty**: 4.5/5 — LLM을 진화 알고리즘의 연산자로 활용하는 완전히 새로운 접근법이나, 실험 범위가 제한적.

- **Technical Soundness**: 4/5 — 기본 방법론은 건실하나, 프롬프트 설계의 과학적 근거 제시 부족, 통계적 유의성 검증 미흡.

- **Significance**: 3.5/5 — 개념적 기여는 의미 있으나 실무적 영향은 현재 제한적. 향후 확장 가능성이 높음.

- **Clarity**: 4/5 — 논문 구조와 설명이 명확하나, 프롬프트 설계 상세 정보 및 LLM 선택 근거 보완 필요.

- **Overall**: 4/5

**총평**: 본 논문은 대규모 언어모델을 진화 알고리즘의 연산자로 활용하는 창의적이고 참신한 패러다임을 제시하며, 추가 훈련 없이 자연어만으로 최적화 문제를 해결할 수 있는 가능성을 보여준다. 다만 제한된 문제 규모와 LLM의 높은 계산 비용이 실제 응용의 장애물이 될 수 있으므로, 향후 대규모 복잡한 실무 문제로의 확장과 프롬프트 최적화 방법론 개발이 필요하다.

## Related Papers

- 🔗 후속 연구: [[papers/466_Large_Language_Model-Based_Evolutionary_Optimizer_Reasoning/review]] — 대형 언어 모델 기반 진화 최적화가 제약 조건이 있는 역합성 계획으로 확장될 수 있습니다.
- 🔄 다른 접근: [[papers/577_Nova_An_iterative_planning_and_search_approach_to_enhance_no/review]] — 조합 최적화에서 LLM 기반 진화 알고리즘과 반복적 계획 및 탐색 접근법을 비교할 수 있습니다.
- 🧪 응용 사례: [[papers/305_Efficient_Evolutionary_Search_Over_Chemical_Space_with_Large/review]] — 대형 언어 모델을 활용한 화학 공간 진화 탐색이 LLM 기반 진화 최적화의 실제 적용 사례입니다.
- 🏛 기반 연구: [[papers/466_Large_Language_Model-Based_Evolutionary_Optimizer_Reasoning/review]] — 대규모 언어모델을 진화 최적화기로 활용하는 일반적인 접근법이 LEO의 구체적인 구현의 이론적 기반을 제공한다.
- 🏛 기반 연구: [[papers/462_Large_Language_Model_Agent_as_a_Mechanical_Designer/review]] — 진화 최적화를 위한 대형 언어 모델이 구조 설계 최적화의 방법론적 기반을 제공합니다.
- 🔗 후속 연구: [[papers/754_ShinkaEvolve_Towards_Open-Ended_And_Sample-Efficient_Program/review]] — LLM을 진화 최적화에 활용하는 기본 아이디어를 ShinkaEvolve가 프로그램 진화에 특화하여 발전시킴
- 🏛 기반 연구: [[papers/472_Large_language_models_design_sequence-defined_macromolecules/review]] — 진화 최적화 알고리즘으로서의 LLM 활용 방법론이 거대분자 설계에 적용된 사례이다.
