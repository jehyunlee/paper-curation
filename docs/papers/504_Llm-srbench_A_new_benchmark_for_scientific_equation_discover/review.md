---
title: "504_Llm-srbench_A_new_benchmark_for_scientific_equation_discover"
authors:
  - "Parshin Shojaee"
  - "Ngoc-Hieu Nguyen"
  - "Kazem Meidani"
  - "Amir Barati Farimani"
  - "Khoa D Doan"
date: "2025"
doi: "arXiv:2504.10415v2"
arxiv: ""
score: 4.4
essence: "본 논문은 대규모 언어 모델(LLM) 기반 과학 방정식 발견의 진정한 능력을 평가하기 위해 암기를 방지하는 종합적 벤치마크 LLM-SRBench를 제안한다. 4개 과학 분야에서 239개 도전 문제로 구성되어 있으며, 최고 성능 모델도 31.5% 기호 정확도에 불과함을 보여준다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/AI_Benchmarking_Taxonomy"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Zhang et al._2025_Llm-srbench A new benchmark for scientific equation discovery with large language models.pdf"
---

# LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models

> **저자**: Parshin Shojaee, Ngoc-Hieu Nguyen, Kazem Meidani, Amir Barati Farimani, Khoa D Doan, Chandan K Reddy | **날짜**: 2025 | **DOI**: [arXiv:2504.10415v2](https://arxiv.org/abs/2504.10415)

---

## Essence

![Figure 1](figures/fig1.webp)
*Figure 1. Feynman 문제와 LLM-SRBench 데이터셋(LSR-Transform, LSR-Synth)에서 단순 LLM 샘플링(Llama-3.1-8B)의 오차 분석. Feynman 문제에서 수치 오차 곡선의 급격한 하강과 낮은 기호 오차는 실제 발견보다 암기를 시사함.*

본 논문은 대규모 언어 모델(LLM) 기반 과학 방정식 발견의 진정한 능력을 평가하기 위해 암기를 방지하는 종합적 벤치마크 LLM-SRBench를 제안한다. 4개 과학 분야에서 239개 도전 문제로 구성되어 있으며, 최고 성능 모델도 31.5% 기호 정확도에 불과함을 보여준다.

## Motivation

- **Known**: LLM이 광범위한 과학 문헌으로 학습되어 방정식 발견에 잠재력이 있음. 기존 벤치마크(SRBench, SRSD)는 잘 알려진 물리 방정식 기반.
  
- **Gap**: 기존 벤치마크는 LLM의 암기에 취약하여 실제 발견 능력이 아닌 단순 암송 능력을 평가함(Fig. 1의 급격한 오차 하강으로 증명). 메모이제이션 방지 문제를 다루는 소규모 커스텀 문제셋만 존재.

- **Why**: LLM 기반 방정식 발견 방법의 진정한 과학적 추론 및 데이터 기반 발견 능력을 엄격하게 평가하는 표준화된 벤치마크가 필요함.

- **Approach**: (1) 익숙한 문제의 비표준 수학적 표현(LSR-Transform), (2) 합성 신규 항을 포함한 발견 주도 문제(LSR-Synth)의 두 가지 카테고리로 암기를 방지하는 벤치마크 설계.

## Achievement

![Figure 2](figures/fig2.webp)
*Figure 2. LLM 기반 과학 방정식 발견의 개요. 벤치마크 과제(좌)에서 과학 맥락과 수치 데이터를 결합하고, 발견 프로세스(중앙)에서 LLM의 과학 지식과 데이터 기반 추론을 활용하여 반복적으로 가설 생성, 평가(우)에서 데이터 신실성, 기호 정확도, 계산 효율성으로 측정.*

1. **종합 벤치마크 구축**: 4개 과학 분야(화학 36, 생물학 24, 물리학 43, 재료과학 25)에서 239개 문제(LSR-Transform 111개, LSR-Synth 128개)로 구성된 첫 번째 대규모 LLM 기반 방정식 발견 벤치마크 제시.

2. **성능 상한선 규정**: 최고 성능 모델(GPT-4o 등)이 LSR-Transform에서 31.5%, LSR-Synth에서 28.1%의 기호 정확도로 현저히 낮은 성능을 달성, 벤치마크의 도전 난이도와 미래 연구 가치 입증.

3. **암기 방지 메커니즘**: Feynman 방정식을 비표준 수학 형태로 변환하고 합성 항을 도입하여 LLM의 단순 암송이 아닌 실제 데이터 기반 추론 능력 평가 가능.

## How

![Figure 3](figures/fig3.webp)
*Figure 3. LLM-SRBench의 두 데이터셋 카테고리에 대한 생성 파이프라인. (a) LSR-Transform은 Feynman 문제를 다른 수학 표현으로 변환.*

### LSR-Transform (변환 기반 문제)

- **Step 1-2**: Feynman 벤치마크의 100개 물리 방정식 수집 후 입력 특성 중 하나를 새로운 목표 변수로 선택
- **Step 3-4**: 원본 목표 변수와 선택된 입력 특성의 역할 교환, SymPy를 사용하여 선택된 변수에 대해 기호적으로 방정식 변환
- **Step 5-7**: 변환된 데이터셋으로 샘플 재생성, 무효 샘플 제거, 과학적 맥락 재작성
- **효과**: 동일한 물리 원리를 다른 수학 형태로 표현하여 암기 우회

### LSR-Synth (합성 신규 문제)

- **Design Philosophy**: 알려진 물리 항과 신규 합성 항 결합으로 진정한 데이터 기반 추론 필요
- **Synthetic Term Creation**: 과학적으로 타당하면서도 교과서에 없는 항 설계
- **Solvability Verification**: 수치 솔버로 생성된 방정식의 물리적 타당성 검증
- **Domain Coverage**: 화학(Arrhenius 방정식 기반), 생물학(Michaelis-Menten 기반), 물리학(고전역학), 재료과학(재료 성질) 등 다양한 분야

### 평가 메트릭

- **Data Fidelity**: 정규화 평균 제곱 오차(NMSE) - 정규 도메인 및 도메인 외 일반화 성능
- **Symbolic Accuracy**: 발견된 기호 표현이 실제 기초 방정식과의 일치도(전문가/LLM 평가)
- **Scientific Plausibility**: 해석 가능성, 과학적 타당성

## Originality

- **LLM 특화 벤치마크 설계**: 기존 SR 벤치마크의 암기 문제를 직접 해결하는 최초의 체계적 방법론 제시
  
- **Dual-Category Framework**: LSR-Transform(익숙한 문제의 비표준 표현)과 LSR-Synth(합성 신규 문제)의 이중 구조로 추론과 발견 능력을 분리 평가

- **Scale & Rigor**: 기존 5개 커스텀 문제에서 239개 문제로 확대, 수치 검증을 통한 물리적 타당성 보장

- **Cross-Domain Coverage**: 물리학 중심에서 벗어나 화학, 생물학, 재료과학까지 확장하여 범용성 확보

## Limitation & Further Study

- **LLM 선택 편향**: 평가된 LLM이 주로 폐쇄형(GPT-4o) 또는 특정 오픈소스 모델(Llama)로 제한되어 향후 다양한 LLM 아키텍처 포함 필요

- **Synthetic Term 설계의 자의성**: 합성 항의 과학적 타당성 판단이 부분적으로 휴리스틱에 기반하여 더 엄격한 물리 기반 생성 방법 개발 필요

- **발견 프로세스의 다양성 부재**: 현재 벤치마크는 단순 LLM 샘플링 기반 평가에 중점으로, 진화 알고리즘 통합 등 하이브리드 방법 평가 부족

- **후속 연구**:
  - LSR-Synth 문제의 자동 생성 알고리즘 개발
  - 다중 단계 추론 및 피드백 루프를 포함한 복잡한 발견 작업 확장
  - 도메인 전이(transfer) 및 일반화 능력 평가 심화

## Evaluation

- **Novelty (독창성)**: 4.5/5 — LLM 기반 방정식 발견 평가를 위한 암기 방지 벤치마크는 신규이며, 이중 카테고리 설계가 체계적이나 기본 아이디어는 기존 연구(Shojaee et al., 2024b)의 확장

- **Technical Soundness (기술적 건전성)**: 4.5/5 — SymPy 기반 변환, 수치 검증, 다중 메트릭 평가 등이 견고하나, 합성 항 생성의 자동화 및 과학적 타당성 보증 메커니즘이 다소 휴리스틱

- **Significance (중요성)**: 4.5/5 — LLM 기반 과학 발견 연구의 핵심 평가 도구로서 장기적 영향 높음. 31.5% 저성능은 미래 개선 방향을 명확히 제시하나, 기존 SR 방법(GP 등)과의 비교 부족

- **Clarity (명확성)**: 4/5 — 전반적으로 구성이 명확하고 Figure 2, 3이 효과적이나, LSR-Synth의 합성 항 설계 원리가 도메인별로 상세히 기술되지 않음

- **Overall: 4.4/5**

**총평**: LLM-SRBench는 과학 방정식 발견 분야에서 실질적 필요에 응하는 도전적이고 엄격한 벤치마크를 제공하며, 암기 방지 설계와 다중 도메인 커버리지가 장점이나, 합성 문제 생성의 자동화 및 기존 SR 방법과의 비교 확대가 후속 개선 과제이다.

## Related Papers

- 🔗 후속 연구: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — 과학적 발견 벤치마킹의 더 넓은 맥락에서 방정식 발견 평가를 포함함
- 🔄 다른 접근: [[papers/289_Drsr_Llm_based_scientific_equation_discovery_with_dual_reaso/review]] — 동일한 과학 방정식 발견 문제를 데이터와 경험 기반 이중 추론으로 접근
- 🧪 응용 사례: [[papers/1083_A_framework_for_discovering_scientific_equations_with_large/review]] — 과학 방정식 발견을 위한 LLM 벤치마크로 실제 평가 시스템 제공
- 🔗 후속 연구: [[papers/012_A_Multi-agent_Framework_for_Physical_Laws_Discovery/review]] — 물리 법칙 자동 발견 프레임워크는 LLM-SRBench의 과학 방정식 발견 벤치마크를 다중 에이전트 협업을 통해 실제 연구 환경으로 확장합니다.
- 🔗 후속 연구: [[papers/289_Drsr_Llm_based_scientific_equation_discovery_with_dual_reaso/review]] — 과학 방정식 발견을 위한 LLM 기반 기호 회귀에서 더 포괄적인 과학 방정식 발견 벤치마크로 확장한 평가 프레임워크입니다.
