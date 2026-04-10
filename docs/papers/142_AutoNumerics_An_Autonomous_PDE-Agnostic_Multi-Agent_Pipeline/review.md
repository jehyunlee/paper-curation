---
title: "142_AutoNumerics_An_Autonomous_PDE-Agnostic_Multi-Agent_Pipeline"
authors:
  - "Jianda Du"
  - "Youran Sun"
  - "Haizhao Yang"
date: "2026.02"
doi: "미공개"
arxiv: ""
score: 4.0
essence: "본 논문은 LLM 기반 다중에이전트 프레임워크를 통해 자연어 기술만으로 일반적인 편미분방정식(PDE)에 대한 투명하고 해석 가능한 수치해석 솔버를 자동으로 설계·구현·검증하는 시스템을 제시한다. 기존 신경망 기반 접근법의 블랙박스성을 극복하고 고전 수치해석의 안정성 보장을 유지하면서 자동화를 달성한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Computational_Fluid_Dynamics"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Du et al._2026_AutoNumerics An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing.pdf"
---

# AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing

> **저자**: Jianda Du, Youran Sun, Haizhao Yang | **날짜**: 2026-02-19 | **DOI**: [미공개](https://doi.org/)

---

## Essence

![AutoNumerics 파이프라인](figures/fig1.webp)
*그림 1: AutoNumerics 파이프라인. 단계 1-4는 문제 공식화 및 계획 선택, 단계 5는 coarse-to-fine 실행 전략, 단계 6-7은 검증 및 이론 분석을 수행한다.*

본 논문은 LLM 기반 다중에이전트 프레임워크를 통해 자연어 기술만으로 일반적인 편미분방정식(PDE)에 대한 투명하고 해석 가능한 수치해석 솔버를 자동으로 설계·구현·검증하는 시스템을 제시한다. 기존 신경망 기반 접근법의 블랙박스성을 극복하고 고전 수치해석의 안정성 보장을 유지하면서 자동화를 달성한다.

## Motivation

- **Known**: 
  - PDE 해결을 위한 전통적 수치해석 방법은 수학적 안정성과 해석성이 우수하나 전문가의 수작업이 필요함
  - PINNs, 연산자 학습 등 신경망 기반 방법은 자동화되었으나 계산 비용이 크고 해석성이 부족함
  - 기존 LLM 기반 PDE 솔루션은 블랙박스 네트워크 생성, 고정된 라이브러리 API 의존, 검증 메커니즘 부족 등의 문제가 있음

- **Gap**: 
  - LLM이 생성한 코드의 디버깅 효율성 (고해상도 그리드에서의 비용 낭비)
  - 해석해가 없는 PDE의 정확성 검증 방법 부재
  - 대규모 시간 진화 시뮬레이션의 메모리 문제

- **Why**: 
  - 기존 방법들은 투명성과 자동화 사이의 트레이드오프가 존재하며, 안정성 보장 없이 자동 생성된 솔버는 종종 실패함

- **Approach**: 
  - 문제 공식화, 계획 생성, 실행, 검증의 다중에이전트 파이프라인
  - Coarse-to-fine 실행 전략으로 로직 버그와 안정성 문제를 분리하여 처리
  - 잔차(residual) 기반 자체 검증 메커니즘
  - 안정성 인식형 계획 생성 및 필터링으로 불안정한 수치 체계 사전 차단

## Achievement

1. **우수한 정확도**: 
   - CodePDE 벤치마크 5개 문제에서 모두 최저 오차 달성 (기하평균 9.00×10⁻⁹)
   - CodePDE 대비 약 6자리 수 개선, FNO 대비 10⁶배 이상 우수
   - 24개 문제 중 19개의 명시해 존재 문제에서 11개가 10⁻⁶ 이상 정확도 달성

2. **체계적 수치 기법 선택**: 
   - Planner Agent가 PDE 특성에 맞는 적절한 수치 기법 자동 선택 (주기경계조건 → Fourier 스펙트럴, Dirichlet경계 포물선형 → 유한차분/요소, 조화연산자 → Chebyshev 스펙트럴)
   - 안정성 위반 솔버 사전 차단으로 중앙차분 방법의 산재 오차(7.05×10¹²) 같은 실패 사례 방지

3. **효율적 자동화**: 
   - 대부분 문제에서 20-130초 내 end-to-end 솔버 생성 완료
   - 200개 PDE 대규모 벤치마크 구성 및 일관된 성능 검증

## How

- **Formulator Agent**: 자연어 기술을 구조화된 PDE 명세(지배방정식, 경계/초기조건, 물리 매개변수)로 변환

- **Planner Agent**: 여러 이산화 방법(유한차분, 스펙트럴, 유한체적)과 시간 적분 전략(명시, 음시)을 포함한 10개 후보 체계 생성, 수치 안정성/일관성 원칙 위반 배제

- **Feature & Selector Agents**: 문제와 제안 체계의 수치적 특성 추출, 상위 5개 계획 선택 전에 부적절한 계획 필터링

- **Coarse-to-fine 실행 전략**:
  - 저해상도 그리드에서 로직 오류(구문 오류, 형상 불일치) 수정 (Critic Agent)
  - 로직 검증 통과 후 고해상도 그리드 실행, 안정성 문제 시 시간 스텝 조정
  - 재시도 초과 시 Fresh Restart로 코드 재생성

- **Residual 기반 검증**:
  - 해석해 존재: 상대 L₂ 오차 (eL₂ = ‖u−u*‖_L₂ / ‖u*‖_L₂)
  - 해석해 부재: 상대 PDE 잔차 (e_res = ‖L(u)−f‖_L₂ / ‖f‖_L₂)
  - 암시적 관계: 상대 암시 잔차 (e_impl = ‖F(u)‖_L₂ / ‖F_ref‖_L₂)

- **메모리 관리**: 대규모 시간 시뮬레이션을 위해 희소 스냅샷 저장 (history decimation)

## Originality

- **다중에이전트 조율 프레임워크**: 문제 공식화부터 검증까지 명확한 역할 분담으로 자동화 달성, 기존 LLM 기반 방법의 단편적 접근과 차별화

- **안정성 인식 계획 생성**: Planner Agent가 수치해석 원리에 기반하여 물리적으로 타당한 체계만 제안, 사전적 불안정성 차단 (새로운 기여)

- **Coarse-to-fine 실행 전략**: 로직 버그와 수치 안정성을 분리하여 처리로 디버깅 효율성 극대화, 계산 낭비 방지 (새로운 기여)

- **잔차 기반 자체 검증**: 해석해 미보유 PDE에 대해 자동 정확성 평가 가능, 기존 방법의 검증 부재 문제 해결 (새로운 기여)

- **대규모 벤치마크**: 200개 PDE 포괄적 벤치마크 구성으로 일반성 체계적 입증

- **해석성 유지**: 신경망 기반 방법과 달리 고전 수치해석 기반 투명한 솔버 코드 생성으로 과학자의 신뢰도 향상

## Limitation & Further Study

- **고차원 및 고차 PDE의 제한**: 5D 이상 고차원 문제(5D Helmholtz: 9.8×10⁻¹)와 4차 PDE(Biharmonic: 6.14×10⁻¹)에서 성능 저하

- **4차 이상 PDE 미흡**: 현재 프레임워크가 2차 이상 PDE에 최적화되어 있으며, 고차 미분 처리의 이산화 복잡성 증대

- **대규모 비선형 PDE**: 복잡한 비선형성을 가진 실무 PDE(예: 난류 모델링)에 대한 성능 평가 부재

- **LLM 의존성**: GPT-4.1에 전적으로 의존하여 모델 변경에 따른 성능 변동성 불명확

- **후속 연구**:
  - 고차원 문제 해결을 위한 차원 축소 기법 또는 다중스케일 방법 통합
  - Adaptive mesh refinement와의 결합
  - 다양한 LLM 모델(Claude, Llama 등)에 대한 강건성 평가
  - 산업 응용(CFD, 재료 과학 등) 맞춤형 PDE 세트 확장


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4/5
- Clarity: 4/5
- Overall: 4/5

**총평**: AutoNumerics는 LLM 기반 자동 PDE 솔버 설계에서 획기적인 진전을 이루었으며, 특히 coarse-to-fine 실행 전략과 안정성 인식형 계획 생성은 실용적으로 탁월한 기여이다. 기존 신경망 기반 방법보다 정확도가 현저히 우수하고(6자리 수) 해석성을 유지한 점이 강점이나, 고차원 및 고차 PDE에 대한 성능 한계와 이론적 수렴성 보장 부재는 개선이 필요하다. 과학 컴퓨팅의 자동화 가능성을 명확히 보여주는 중요한 작업이지만, 실제 산업 응용을 위해서는 추가 검증과 확장이 요구된다.

## Related Papers

- 🏛 기반 연구: [[papers/722_Scifibench_Benchmarking_large_multimodal_models_for_scientif/review]] — AutoNumerics의 PDE 해석 자동화는 SciFIBench의 과학적 그림 이해 벤치마크에서 검증된 멀티모달 과학적 추론 능력을 수치해석 영역에 적용합니다.
- 🧪 응용 사례: [[papers/721_Scientific_Machine_Learning_through_Physics-Informed_Neural/review]] — AutoNumerics는 Physics-Informed Neural Networks의 과학적 기계학습 원리를 실제 PDE 솔버 자동 생성 시스템에 적용하여 이론과 실무를 연결합니다.
- 🧪 응용 사례: [[papers/169_Bioprobench_Comprehensive_dataset_and_benchmark_in_biologica/review]] — 자율적 다중 에이전트 시스템을 생물학적 실험 프로토콜 수행에 적용할 수 있다
