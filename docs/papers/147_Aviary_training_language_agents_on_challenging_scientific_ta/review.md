---
title: "147_Aviary_training_language_agents_on_challenging_scientific_ta"
authors:
  - "Siddharth Narayanan"
  - "James D. Braza"
  - "Ryan-Rhys Griffiths"
  - "Manu Ponnapati"
  - "Albert Bou"
date: "2024.12"
doi: "N/A"
arxiv: ""
score: 4.3
essence: "본 논문은 과학적 작업을 해결하기 위한 언어 에이전트(language agent)를 훈련하기 위한 확장 가능한 체육관 프레임워크인 Aviary를 제시한다. 저자들은 언어 에이전트를 언어-기반 부분 관찰 가능 마르코프 결정 과정(language decision process, LDP)으로 형식화하고, DNA 조작, 과학 문헌 질문 응답, 단백질 안정성 공학 등 3개의 과학 환경을 포함한 5개 환경을 구현했다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Realistic_Discovery_Benchmarks"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Narayanan et al._2024_Aviary training language agents on challenging scientific tasks.pdf"
---

# Aviary: training language agents on challenging scientific tasks

> **저자**: Siddharth Narayanan, James D. Braza, Ryan-Rhys Griffiths, Manu Ponnapati, Albert Bou, Jon Laurent, Ori Kabeli, Geemi Wellawatte, Sam Cox, Samuel G. Rodriques, Andrew D. White | **날짜**: 2024-12-30 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: 5개의 Aviary 환경과 언어 결정 과정(LDP) 프레임워크 개요*

본 논문은 과학적 작업을 해결하기 위한 언어 에이전트(language agent)를 훈련하기 위한 확장 가능한 체육관 프레임워크인 Aviary를 제시한다. 저자들은 언어 에이전트를 언어-기반 부분 관찰 가능 마르코프 결정 과정(language decision process, LDP)으로 형식화하고, DNA 조작, 과학 문헌 질문 응답, 단백질 안정성 공학 등 3개의 과학 환경을 포함한 5개 환경을 구현했다.

## Motivation

- **Known**: 언어 모델(LLM)은 뛰어난 0-shot 일반화 능력을 가지지만, 고립된 상태에서는 추론 오류를 보인다. 최근 언어 에이전트는 내부 추론, 계획, 도구 사용 등을 통해 환경과 상호작용하며 개선되고 있다.

- **Gap**: 언어 에이전트에 대한 통일된 이론적 프레임워크가 부족하며, 다양한 구성 요소(추론, 계획, 도구 사용, LLM 샘플링 파라미터)를 효율적으로 최적화하기 위한 일관된 소프트웨어 구현이 미흡하다.

- **Why**: 과학적 작업은 다단계 추론과 도구 사용이 필수적이며, 이를 체계적으로 평가하고 훈련할 수 있는 통합 프레임워크가 필요하다.

- **Approach**: 언어 에이전트를 확률적 계산 그래프(stochastic computation graph)로 표현하여 LDP로 정의하고, 확장 가능한 환경 프레임워크(Aviary)를 구축하여 expert iteration 등의 최적화 기법을 적용한다.

## Achievement

![Figure 3](figures/fig3.webp)
*그림 3: Aviary 환경을 사용하여 LLM과 언어 에이전트의 작업 해결 능력*

1. **이론적 기여**: 부분 관찰 가능 마르코프 결정 과정(POMDP)의 자연언어 표현으로서 언어 결정 과정(LDP)을 형식화하여, 다양한 기존 에이전트 아키텍처(CoALA, ReAct 등)를 통일된 프레임워크로 구현 가능함을 시연했다.

2. **성능 달성**: 오픈 소스 소형 모델(Llama-3.1-8B-Instruct)을 온라인 훈련(expert iteration)과 추론 시간 샘플링(majority vote)으로 훈련하여, DNA 구축 설계 및 과학 문헌 질문 응답 환경에서 최첨단 LLM(GPT-4o 등)과 인간 전문가를 능가하면서 **추론 비용을 100배 감소**시켰다.

## How

![Figure 2](figures/fig2.webp)
*그림 2: 확률적 계산 그래프로 표현된 단순 언어 에이전트 아키텍처*

- **LDP 형식화**: 상태 공간 S, 자연언어 기반 행동 공간 A, 관찰 공간 O, 전이 함수 T, 보상 함수 R, 할인 계수 γ로 구성된 튜플 (V, S, A, O, T, Z, R, γ)로 정의. 정책 π_θ: O → A는 학습 가능한 파라미터 θ(LLM 가중치, 온도 등)를 포함.

- **5개 환경 구현**: (1) 분자 클로닝 DNA 구축(SeqQA), (2) 과학 문헌 질문 응답(LitQA2), (3) 단백질 안정성 공학(ProteinBench), (4) GSM8K(수학 추론), (5) HotpotQA(다중홉 질문 응답)

- **훈련 파이프라인**: Expert iteration을 통해 자가 생성 궤적에 대한 지도 학습(supervised fine-tuning)으로 반복적 개선. 추론 시점에서 majority vote 샘플링으로 성능 향상.

- **모듈식 설계**: Aviary (환경 정의), LDP (에이전트 및 최적화기 구현)로 분리하여 환경, 에이전트, 옵티마이저의 교환 가능성 제공.

![Figure 4](figures/fig4.webp)
*그림 4: (A) 분자 클로닝 환경에서 SeqQA 작업 훈련, (B) LitQA2 작업 훈련*

## Originality

- **이론적 독창성**: LDP를 명시적으로 형식화하고 부분 관찰 가능성과 자연언어 관찰의 특성을 강조한 점. 기존 POMDP 프레임워크보다 언어 에이전트의 특수성을 더 정확히 포착.

- **소프트웨어 아키텍처**: 환경과 에이전트 최적화 프레임워크를 명확히 분리한 설계는 기존 LangChain, LlamaIndex, DSPy 등과 차별화되며, 확률적 계산 그래프를 통해 다양한 구성 요소(메모리, 추론, 도구 사용, 샘플링 파라미터) 최적화의 일관된 처리.

- **과학 환경 큐레이션**: DNA 분자 클로닝, 단백질 안정성 공학 등 실제 생물학 연구와 관련된 도메인별 환경으로, 기존 벤치마크보다 더 구체적이고 다단계 추론을 요구.

- **실증적 성과**: 소형 오픈 소스 모델이 최첨단 상용 모델을 능가할 수 있음을 체계적으로 입증한 점.

## Limitation & Further Study

- **환경 복잡도 제한**: 본 논문은 결정론적 환경을 중심으로 하며, 확률적 환경(실험 오류, 불확실한 결과)에서의 에이전트 성능은 미검증.

- **확장성 미검토**: 현재 가장 복잡한 환경에서도 단계 수가 제한적이며, 더 긴 수평선(long-horizon)의 작업에서 성능이 어떻게 변하는지는 불명확.

- **이론적 완성도**: 추론 시점 샘플링의 최적 전략(다수결 투표 수, 온도 설정)에 대한 이론적 분석 부족. 언어 에이전트의 정보 이론적 특성(예: 자연언어 표현의 압축 효율)에 대한 탐구 필요.

- **도메인 전이성**: 훈련된 에이전트가 다른 과학 도메인(화학, 물리학 등)으로 전이될 수 있는지, 또는 도메인별 재훈련이 필수인지는 미검토.

- **인간-에이전트 협업**: 에이전트가 인간 전문가를 능가하는 환경에서도, 협업 시나리오에서의 상호 작용 메커니즘 미탐색.

## Evaluation

- **Novelty (독창성)**: 4.5/5
  - LDP 형식화와 확률적 계산 그래프 프레임워크는 명확하고 포괄적. 다만, POMDP 개념 자체는 기존이며, 자연언어 특수성 강조가 주요 기여.

- **Technical Soundness (기술적 건전성)**: 4.5/5
  - 수학적 형식화는 엄밀하고 구현은 체계적. 다만, expert iteration의 수렴성 증명 부재, 추론 시점 샘플링의 이론적 정당화 미흡.

- **Significance (중요성)**: 4.5/5
  - 과학 자동화라는 중요한 응용 분야에 체계적 접근. 소형 모델의 경제성 입증은 실무 임팩트가 높음. 다만, 현재 환경이 생물학 특화로 다른 과학 분야 적용성은 미지수.

- **Clarity (명확성)**: 4/5
  - 논문 전체 구조가 명확하고 그림이 잘 배치됨. 다만, LDP와 POMDP의 구체적 차이점, 상태 공간 S의 구체적 정의가 환경별로 더 명확히 제시되면 이해가 용이.

- **Overall (종합)**: 4.3/5

**총평**: 본 논문은 언어 에이전트를 위한 명확한 이론적 틀(LDP)과 실용적 구현(Aviary)을 제공하며, 과학 작업의 자동화라는 중요한 응용에서 경제성 높은 성과를 달성했다. 특히 오픈 소스 소형 모델의 잠재력을 입증한 점이 주목할 만하나, 환경 확장성, 이론적 분석 심화, 다중 도메인 검증 등 향후 연구가 필요하다.

## Related Papers

- 🏛 기반 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 언어 에이전트의 머신러닝 능력 평가를 과학적 작업이라는 더 도전적인 환경으로 확장한다.
- 🔗 후속 연구: [[papers/704_SciAgentGym_Benchmarking_Multi-Step_Scientific_Tool-use_in_L/review]] — 기본적인 과학적 작업 훈련을 다단계 도구 활용을 포함한 복합적 과학적 추론으로 발전시킨다.
- 🧪 응용 사례: [[papers/828_Towards_end-to-end_automation_of_AI_research/review]] — 과학적 작업에서 훈련된 언어 에이전트가 완전 자동화된 과학 연구의 핵심 구성요소로 활용될 수 있음을 보여준다.
- 🔄 다른 접근: [[papers/717_Scienceboard_Evaluating_multimodal_autonomous_agents_in_real/review]] — 과학 언어 에이전트 훈련을 위해 현실적 워크플로우 평가와 도전적 과학 작업이라는 다른 접근법을 사용한다
