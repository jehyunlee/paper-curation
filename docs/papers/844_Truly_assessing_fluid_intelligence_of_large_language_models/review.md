---
title: "844_Truly_assessing_fluid_intelligence_of_large_language_models"
authors:
  - "Yue Yang"
  - "Mingkang Chen"
  - "Qihua Liu"
  - "Mengkang Hu"
  - "Qiguang Chen"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.4
essence: "본 논문은 대규모 언어모델(LLM)의 진정한 유동 지능(fluid intelligence)을 평가하기 위해 계층적 인지 프레임워크를 바탕으로 한 동적 추론 평가 벤치마크 **DRE-Bench**를 제안한다. 4가지 인지 수준(속성, 공간, 순차, 개념)의 36개 추상 추론 과제와 복잡도 변화를 포함한 약 4,000개의 사례를 통해 LLM의 규칙 일반화 능력을 체계적으로 측정한다."
tags:
  - "cat/Cognitive_AI_Evaluation_and_Benchmarking"
  - "sub/Working_Memory_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Yang et al._2025_Truly assessing fluid intelligence of large language models through dynamic reasoning evaluation.pdf"
---

# Truly assessing fluid intelligence of large language models through dynamic reasoning evaluation

> **저자**: Yue Yang, Mingkang Chen, Qihua Liu, Mengkang Hu, Qiguang Chen, Gengrui Zhang, Shuyue Hu, Guangtao Zhai, Yu Qiao, Yu Wang, Wenqi Shao, Ping Luo | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: (a) 숨겨진 잠재 규칙의 예시, (b) 기존 벤치마크와의 비교, (c) DRE-Bench의 LLM 지능 리더보드*

본 논문은 대규모 언어모델(LLM)의 진정한 유동 지능(fluid intelligence)을 평가하기 위해 계층적 인지 프레임워크를 바탕으로 한 동적 추론 평가 벤치마크 **DRE-Bench**를 제안한다. 4가지 인지 수준(속성, 공간, 순차, 개념)의 36개 추상 추론 과제와 복잡도 변화를 포함한 약 4,000개의 사례를 통해 LLM의 규칙 일반화 능력을 체계적으로 측정한다.

## Motivation

- **Known**: 최근 LLM들(GPT-4o, o1, DeepSeek-R1 등)이 인상적인 추론 능력을 보여주고 있으며, 기존 AIME, GPQA 같은 벤치마크에서 전문가 수준의 성능을 달성하고 있다.

- **Gap**: 기존 추론 벤치마크들은 다음 세 가지 한계를 가진다: (1) 추상 추론 과제들이 인간의 인지 단계와 연결되지 않아 해석 가능성 부족, (2) 수작업 주석으로 인한 확장성 제한, (3) 정적(static) 특성으로 인한 데이터 오염(contamination) 문제와 단일 복잡도 수준.

- **Why**: 진정한 유동 지능은 기억된 내용을 넘어 새로운 상황에서 추론하고 규칙을 일반화하는 능력이다. LLM이 규칙을 진정으로 이해했는지 아니면 단순히 암기했는지 구분하기 위해 복잡도 변화와 인지 계층 구조가 필요하다.

- **Approach**: 확인된 심리학 계층 구조(Primi, 2001)에 기반하여 4가지 인지 수준으로 조직된 36개 추상 추론 과제를 설계하고, 각 과제에 대해 코드 기반 생성기와 해결기를 개발하여 동적으로 다양한 복잡도의 변형 사례를 자동 생성한다.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 4가지 인지 수준에 걸친 구체적인 추상 추론 과제들 및 동적 변수 예시*

1. **계층적 인지 정렬 평가 체계 구축**: 속성(Attribute) → 공간(Spatial) → 순차(Sequential) → 개념(Conceptual) 수준의 4단계 인지 계층 구조 내 36개 과제 설계. 각 수준은 특정 인지 능력(대칭, 회전, 중력, 팽창 등)을 체계적으로 평가한다.

2. **동적 데이터 생성 엔진 개발**: LLM 기반 에이전트가 설계한 코드 생성기/해결기를 통해 약 4,000개의 검증된 추상 추론 사례를 자동 생성. 각 과제마다 매개변수 변화(크기, 개수, 단계, 각도 등)로 복잡도 조절이 가능하여 데이터 오염 문제 해결.

3. **LLM 유동 지능의 구체적 한계 규명**: 
   - 인지 수준이 높아질수록 모든 모델의 정확도가 급격히 저하 (특히 물리 개념 관련 과제)
   - 추론 LLM(o1, DeepSeek-R1)이 일반 LLM(Claude 3.7, GPT-4o)보다 우수하나, 고수준 과제에서도 성능 한계 명확
   - 복잡도 증가 시 성능 저하 모델은 진정한 규칙 습득이 아닌 부분적 패턴 인식만 가능

## How

![Figure 3](figures/fig3.webp)
*그림 3: DRE-Bench 데이터 생성 파이프라인*

- **계층적 과제 설계**: 인지 심리학 문헌(Primi, 2001)에서 검증된 4단계 인지 수준을 참고하여 각 수준당 3개의 잠재 규칙(latent rule) 정의

- **인간-에이전트 협력 파이프라인**: 
  - 전문가가 각 과제의 제약 조건과 규칙 정의
  - LLM 에이전트가 규칙 기반 코드 생성기 작성 (입력 샘플 생성)
  - LLM 에이전트가 코드 기반 해결기 작성 (정답 생성)
  - 자동 검증 및 품질 관리

- **동적 복잡도 변화 메커니즘**: 각 과제마다 주요 매개변수(size, number, angle, steps, times 등)를 변경하여 동일 잠재 규칙 하에서 저/중/고 복잡도의 변형 생성

- **평가 방법론**:
  - 정확도 측정: 각 인지 수준별 성능 평가
  - 분산 측정: 복잡도 변화에 따른 성능 안정성 평가 (분산이 작을수록 진정한 규칙 습득)
  - 맥락 내 학습(in-context learning) 효과, 시각 정보 유용성, 추론 시간 스케일링 분석

## Originality

- **인지 심리학 기반 계층 구조**: 기존 벤치마크의 단순 난이도 분류가 아닌 확인된 심리학 이론(Primi, 2001의 인지 능력 분류)에 기반한 체계적 계층화로, LLM 능력을 인간 인지와 직접 비교 가능하도록 함

- **자동화된 동적 데이터 생성**: 코드 기반 생성기/해결기를 통한 완전히 자동화된 데이터 생성으로 확장성 문제 해결. 수작업 주석의 한계를 극복하면서 생성된 모든 사례의 정확성 보장

- **복잡도 기반 일반화 평가**: 동일 잠재 규칙의 다양한 복잡도 변형을 통해 단순 암기가 아닌 진정한 규칙 이해 여부를 판단하는 새로운 평가 방식 제시

- **대규모 실증 분석**: GPT-4o, Claude 3.7, o1, DeepSeek-R1, QwQ, Skywork-OR1 등 7개 주요 LLM의 체계적 비교로 현재 LLM의 유동 지능 수준 객관화

## Limitation & Further Study

- **과제 설계의 제한성**: 본 벤치마크는 시각 그리드 기반 추상 추론에 국한되어 있으며, 언어 기반의 다른 유형의 추론(논리적 추론, 수학적 증명 등)에는 직접 적용이 어려울 수 있다.

- **시각 정보의 효과성 미해결**: 논문에서 시각 정보 추가가 정확도를 오히려 낮춘다는 역직관적 결과를 보고했으나, 이에 대한 깊이 있는 분석이 부족하다. 향후 멀티모달 모델의 발전과 함께 이 현상을 재검토할 필요가 있다.

- **고수준 과제 성능 부족의 원인 분석 부재**: LLM이 개념 수준 과제에서 저조한 성능을 보이는 정확한 원인(모델 구조 문제, 학습 데이터 부족, 추론 방식의 근본적 한계 등)에 대한 상세 분석이 필요하다.

- **인간 성능 비교 부족**: LLM 성능을 인간 벤치마크(특히 IQ 테스트의 평균 성능)와 직접 비교하지 않아, "진정한 인간 수준"이 구체적으로 무엇인지 명확하지 않다.

- **후속 연구 방향**:
  - 물리 시뮬레이션 기반의 더 복잡한 개념 수준 과제 개발
  - 인간 피험자 실험을 통한 인간-LLM 성능 비교
  - 모델 내부 표현(representation) 분석을 통한 실패 원인 규명
  - 강화 학습을 통한 LLM의 유동 지능 개선 방안 연구

## Evaluation

- **Novelty**: 4.5/5
  - 인지 심리학 기반 계층 구조와 자동화된 동적 생성의 조합이 기존 벤치마크 대비 신선함
  - 다만 추상 추론 평가 자체는 ARC의 확장이므로 완전히 새로운 영역은 아님

- **Technical Soundness**: 4.5/5
  - 코드 기반 생성기/해결기의 검증 방법론이 명확하고, 대규모 실증 평가가 체계적
  - 다만 LLM 에이전트를 통한 생성 과정에서의 잠재적 오류나 바이어스에 대한 논의가 부족

- **Significance**: 4.5/5
  - LLM의 추론 능력 평가에 새로운 표준을 제시하고, ICLR 2026 출판으로 학계 영향력 확보
  - 연속적이고 복잡도 조절 가능한 평가 체계는 향후 LLM 개발의 중요한 참고 자료가 될 것
  - 다만 실제 산업 응용과의 연결성은 다소 제한적

- **Clarity**: 4/5
  - Figure 1-2의 시각화가 명확하고 네 가지 인지 수준의 정의가 체계적
  - 논문의 동기, 방법론, 결과가 일관되게 흐름
  - 다만 기술적 세부사항(생성기/해결기 구현, 검증 기준)에 대한 설명은 부록 참조 필요

- **Overall**: 4.4/5

**총평**: 본 논문은 LLM의 진정한 유동 지능 평가를 위해 인지 심리학 기반의 계층적 구조와 동적 데이터 생성 엔진을 결합한 혁신적인 벤치마크를 제시한다. 광범위한 모델 평가를 통해 현재 LLM의 근본적인 한계를 명확히 규명했으며, 이는 향후 추론 능력 강화 연구의 객관적 기준점이 될 것으로 기대된다. 다만 평가 범위의 확장성과 실패 원인 분석의 깊이 측면에서 추가 개선의 여지가 있다.

## Related Papers

- 🏛 기반 연구: [[papers/879_What_factors_affect_multimodal_in-context_learning_an_in-dep/review]] — 멀티모달 맥락에서 유동 지능 평가의 기반 연구가 됨
- 🔗 후속 연구: [[papers/652_Rbf_Quantifying_and_optimizing_reasoning_boundaries_across_m/review]] — 추론 경계 최적화가 유동 지능의 동적 추론 평가를 확장함
- 🔗 후속 연구: [[papers/879_What_factors_affect_multimodal_in-context_learning_an_in-dep/review]] — 유동 지능 연구의 멀티모달 확장으로 인-컨텍스트 학습 요소 분석
- 🏛 기반 연구: [[papers/652_Rbf_Quantifying_and_optimizing_reasoning_boundaries_across_m/review]] — 대형 언어모델의 유동 지능 평가는 추론 경계 정량화를 위한 근본적인 인지 능력 측정 기준을 제공합니다
