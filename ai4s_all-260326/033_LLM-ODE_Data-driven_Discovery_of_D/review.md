# LLM-ODE: Data-driven Discovery of Dynamical Systems with Large Language Models

> **저자**: Amirmohammad Ziaei Bideh, Jonathan Gryak | **날짜**: 2026-03-21 | **arXiv**: 2603.20910 | **학회**: GECCO '26

---

## Essence

동역학 시스템의 지배 방정식(ODE)을 관측 궤적 데이터로부터 자동 발견하기 위해 LLM을 genetic programming(GP)의 진화 연산자로 활용하는 하이브리드 프레임워크 LLM-ODE를 제안한다. 기존 GP의 무작위 mutation/crossover를 LLM이 생성하는 구조적으로 informed된 제안으로 대체하여, 기호식(symbolic expression) 탐색 효율을 크게 향상시켰다. 91개 동역학 시스템(1~4차원, 혼돈 역학 포함) 벤치마크에서 LLM-ODE가 PySR, SINDy, ODEFormer를 탐색 효율과 Pareto front 품질 측면에서 일관적으로 능가한다.

## Motivation

- **알려진 것**: GP 기반 symbolic regression이 데이터로부터 해석 가능한 방정식을 발견하는 가장 정확한 방법 중 하나이나, 기호식 공간의 비효율적 탐색으로 수렴이 느리고 확장성이 부족. SINDy는 선형 조합 가정이 제한적이고, Transformer 기반 방법(ODEFormer)은 직접적 추론 정확도에 한계
- **Gap**: 기존 LLM 기반 symbolic regression은 단일 방정식 발견에 국한되었으며, 연립 미분방정식(coupled ODE system)으로의 확장이 부재
- **왜 중요한가**: 물리, 생물, 화학, 공학 등 다양한 과학 분야에서 동역학 시스템의 지배 방정식 자동 발견은 과학적 이해와 예측의 핵심 과제
- **접근법**: LLM의 generative prior를 GP의 진화 연산자로 통합하여, elite 후보 방정식의 패턴을 학습한 구조적 제안으로 탐색 효율 향상

## Achievement

1. **광범위한 벤치마크 우위**: 91개 동역학 시스템에서 LLM-ODE 변형들이 거의 모든 차원/정밀도 조건에서 PySR 대비 높거나 동등한 발견율 달성
2. **빠른 수렴**: LLM-ODE가 50 iteration 내에 달성하는 발견율을 PySR는 200 iteration 후에도 도달하지 못하는 경우가 다수 (예: NMSE 10^-3, 10^-5)
3. **고차원 확장성**: D=4에서 SINDy 성능이 붕괴하는 반면, LLM-ODE는 여러 시스템을 성공적으로 복원. PySR 대비도 현저한 우위
4. **Pareto front 다양성**: 초기 학습 단계에서 LLM-ODE가 PySR 대비 훨씬 풍부한 시스템 Pareto front를 생성하여, 더 효과적인 탐색 공간 커버리지 시사
5. **다중 LLM 검증**: Qwen, Mistral, Olmo 3종 LLM 모두에서 일관된 개선 확인

## How

- **프레임워크**: Island-based evolutionary strategy + LLM-guided evolution
  - 4개 독립 island, 각 2개 seed expression으로 초기화, 200 iteration 진화
  - 각 iteration에서 softmax 가중 샘플링으로 k=8개 elite 방정식 선택 → LLM에 in-context example로 제공 → b=3개 새 후보식 생성
  - 후보식의 상수(C)를 BFGS 최적화로 fitting
  - 5 iteration마다 island 간 방정식 교환 및 pruning (refinement)
- **시스템 구성**: 각 상태 변수별로 독립적으로 symbolic regression 수행 → Cartesian product로 시스템 조합 → 시스템 수준 Pareto front에서 최적 트레이드오프 선택 (max marginal gain in trajectory fitness per unit complexity)
- **Memorization 방지**: 시스템 설명, 변수명, 물리적 단위 등 메타데이터를 프롬프트에서 완전 제거
- **평가 지표**: Normalized MSE(NMSE) 기반 발견 성공률, 수렴 속도, Pareto front 크기
- **Baseline**: PySR (GP), SINDy (선형 모델), ODEFormer (Transformer LSPT)

## Originality

- **연립 ODE 발견을 위한 최초의 LLM-GP 하이브리드**: 기존 LLM-SR이 단일 방정식에 국한된 것을 시스템 수준으로 확장한 최초의 연구. Cartesian product 기반 시스템 조합과 2단계 Pareto front 선택이 핵심
- **LLM as Evolutionary Operator**: 무작위 mutation/crossover 대신 LLM의 in-context learning을 활용하여 구조적으로 의미 있는 변형을 제안하는 방식. 기존 GP의 탐색 비효율성을 직접적으로 해결
- **Memorization-aware 실험 설계**: 변수명 등 의미 정보를 제거하여 LLM의 기억 활용을 방지한 공정한 평가 프로토콜

## Limitation & Further Study

### 저자들이 언급한 한계

- LLM 추론의 latency가 computational bottleneck으로, 비LLM GP 대비 실행 속도가 느림
- LLM 실행에 특수 하드웨어 필요하여 접근성 제한 (양자화/low-rank 근사로 완화 가능)

### 자체판단 아쉬운 점

- **변수 분해의 한계**: 각 상태 변수를 독립적으로 symbolic regression한 후 Cartesian product로 조합하는 방식이, 변수 간 강한 coupling이 있는 시스템에서 최적이 아닐 수 있음. 연립 방정식의 구조적 제약(보존량, 대칭성 등)을 활용하지 못함
- **D=3, D=4에서의 절대 성능 부족**: 고차원에서 LLM-ODE도 발견율이 크게 하락 (D=3에서 NMSE 10^-4 기준 최대 2개, D=4에서 3개). 상대적 우위는 있으나 절대적 발견 능력은 여전히 제한적
- **단일 궤적 학습**: 하나의 초기 조건에서 생성된 궤적만으로 학습하므로, 다중 궤적을 활용한 더 robust한 발견 가능성을 놓침
- **비용 분석 부재**: LLM 호출 횟수, API 비용, 총 실행 시간 등의 구체적 비용 비교가 없어, 실용적 효율성 판단이 어려움
- **Noise robustness 미검증**: 모든 실험이 clean simulation data에서 수행되어, 실험 데이터의 노이즈에 대한 강건성이 불명

### 후속 연구

- 실제 미지의 과학 시스템에 적용하되, 시스템 메타데이터를 LLM에 제공하여 도메인 지식 활용
- 노이즈 있는 실험 데이터에서의 robustness 검증
- LLM 추론 비용 절감을 위한 경량 모델 및 캐싱 전략 개발

## Evaluation

| 항목 | 점수 |
|------|------|
| Novelty | 4/5 |
| Technical Soundness | 4/5 |
| Significance | 4/5 |
| Clarity | 4/5 |
| Overall | 4/5 |

**총평**: GP의 무작위 진화 연산자를 LLM의 구조적 제안으로 대체한다는 아이디어가 명확하고 효과적이며, 91개 동역학 시스템에 대한 포괄적 벤치마크와 3종 LLM 비교가 실험의 신뢰성을 높인다. 연립 ODE 시스템 발견으로의 확장이 기존 LLM-SR 대비 중요한 진전이다. 고차원에서의 절대 성능과 실험 데이터 적용 가능성은 향후 과제로 남지만, LLM을 과학적 방정식 발견의 지능형 탐색 도구로 활용하는 방향성을 잘 제시한 연구이다.
