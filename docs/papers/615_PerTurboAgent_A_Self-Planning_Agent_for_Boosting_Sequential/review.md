---
title: "615_PerTurboAgent_A_Self-Planning_Agent_for_Boosting_Sequential"
authors:
  - "Minsheng Hao"
  - "Yongju Lee"
  - "Hanchen Wang"
  - "Gabriele Scalia"
  - "Aviv Regev"
date: "2025"
doi: "10.1101/2025.05.25.656020"
arxiv: ""
score: 4.0
essence: "대규모 유전자 섭동 실험(Perturb-seq)에서 제한된 실험 자원 내에서 최대의 정보 수집을 위해, 자기 계획 능력을 갖춘 LLM 기반 에이전트(PerTurboAgent)를 개발하여 순차적 유전자 선택 문제를 자동화하고 기존 능동학습(active learning) 방법들을 능가하는 성능을 달성했다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/AI_Research_Ideation"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Hao et al._2025_PerTurboAgent A Self-Planning Agent for Boosting Sequential Perturb-seq Experiments.pdf"
---

# PerTurboAgent: A Self-Planning Agent for Boosting Sequential Perturb-seq Experiments

> **저자**: Minsheng Hao, Yongju Lee, Hanchen Wang, Gabriele Scalia, Aviv Regev | **날짜**: 2025 | **DOI**: [10.1101/2025.05.25.656020](https://doi.org/10.1101/2025.05.25.656020)

---

## Essence

![Figure 1](figures/fig1.webp)
*PerTurboAgent 개요: 자기 계획 능력을 갖춘 LLM 기반 에이전트가 순차적 실험 라운드를 통해 표적 페놀타입에 영향을 미치는 유전자 섭동을 식별*

대규모 유전자 섭동 실험(Perturb-seq)에서 제한된 실험 자원 내에서 최대의 정보 수집을 위해, 자기 계획 능력을 갖춘 LLM 기반 에이전트(PerTurboAgent)를 개발하여 순차적 유전자 선택 문제를 자동화하고 기존 능동학습(active learning) 방법들을 능가하는 성능을 달성했다.

## Motivation

- **Known**: Perturb-seq는 CRISPR 기반 대규모 유전자 스크리닝으로 수천 개 유전자의 섭동이 표현형에 미치는 영향을 scRNA-seq으로 측정할 수 있으며, 최근 생성형 모델들이 미측정 섭동의 영향을 예측하려고 시도하고 있음

- **Gap**: 가능한 모든 유전자 조합의 섭동을 전수 실험하는 것은 불가능하고, 제한된 실험 예산 내에서 어떤 유전자를 선택할지 결정하는 것이 주요 병목. 기존 활성학습 방법들은 예측 모델 성능 향상에만 집중하거나 생물학적 지식을 충분히 활용하지 못함

- **Why**: 유전자 회로의 모듈성과 희소성을 고려하면, 제한된 실험으로도 전체 섭동 공간을 학습할 수 있으나, 이를 위해서는 (1) 이전 지식과 새 데이터의 통합, (2) 통계 분석과 머신러닝 예측의 조합, (3) 실험 결과의 반영적 해석이 필요함

- **Approach**: LLM 에이전트의 추론 능력과 도구 사용 능력(tool use)을 활용하여 자기-계획(self-planning) 메커니즘을 구현하고, 행동 메모리(action memory)를 통해 다단계 의사결정을 지원하는 방식

## Achievement

![Figure 2](figures/fig2.webp)
*라운드별 Hit 누적 곡선: PerTurboAgent가 기존 능동학습 방법(GeneDisco, DiscoBAX, Iterpert)과 다른 LLM 에이전트(BioDiscoveryAgent)를 일관되게 능가*

1. **성능 우월성**: 11개 표현형 과제에서 PerTurboAgent가 기존 활성학습 방법들(GeneDisco, DiscoBAX, Iterpert)과 최근 BioDiscoveryAgent를 일관되게 능가하며, 특히 초기 라운드에서 더 빠르게 hit 유전자를 식별

2. **해석 가능성과 투명성**: 선택된 행동의 빈도 분석과 내부 메모리 추적을 통해 에이전트의 추론 과정을 명확히 가시화할 수 있으며, 구체적인 행동 로그(Figure 4)를 통해 의사결정 근거를 추적 가능

3. **모델 호환성**: 폐쇄형(GPT-4) 및 개방형(Llama) 모델 모두에서 작동하며, 더 고급 모델을 사용할수록 성능이 향상되는 특성을 보임

## How

![Figure 3](figures/fig3.webp)
*PerTurboAgent 행동 분석: (a) 범주별 행동 수 분포 (추론, ML 추론, 분석) (b) 라운드별 행동 빈도 변화*

- **행동 풀(Action Pool) 설계**: 세 가지 범주로 구성
  - **추론(Reasoning)**: 메모리 내 결과 반영(reflection), 예측 정제(refinement), 다음 실험 계획
  - **ML 추론(ML Inference)**: 섭동 예측 모델 훈련, 새로운 섭동 예측
  - **분석(Analysis)**: GSEA(Gene Set Enrichment Analysis), 양성/음성 hit 섭동에 대한 풍부성 검사, 제어군 및 섭동군 유전자 발현 분석

- **행동 메모리 메커니즘**: 각 라운드 내에서 K단계마다 수행한 행동과 그 결과를 메모리에 저장하여, 이후 단계의 의사결정이 이전 결과에 적응적으로 진화할 수 있도록 지원

- **작업 초기화(Task Initialization)**: 
  - 표적 페놀타입명과 관련 기술 유전자(ADGs: Associated Descriptive Genes) 제공
  - 사용자는 사전 지식 기반 또는 기존 Perturb-seq 결과로부터 ADG 정의 가능

- **페놀타입 점수(Phenotype Score)**: 섭동 후 P에 속한 유전자들의 표현 변화를 z-score 기준으로 정량화하여 섭동의 강도 평가

- **순차 선택 프로세스**: 
  - R=0에서 제어군 유전자 발현 Gc 수신
  - R≥1에서 선택된 m개 유전자의 섭동군 발현 Gp 수신
  - 각 유전자는 최대 1회만 선택 가능 (I_untested에서만 선택)

## Originality

- **LLM 에이전트의 자기 계획 능력**: 기존 BioDiscoveryAgent의 고정된 계획과 달리, PerTurboAgent는 매 단계마다 문맥과 누적된 행동 결과에 따라 다음 행동을 동적으로 결정하는 자기-계획(self-planning) 메커니즘 도입

- **다층적 행동 풀 구성**: 추론, ML 추론, 분석의 세 범주로 나뉘어진 행동들을 유연하게 조합하여 상황별 최적 전략을 자동으로 선택할 수 있는 구조로, 기존 방법들의 단순한 단계별 선택과 차별화

- **생물학적 지식과 데이터 기반 접근의 통합**: 사전 지식(KEGG 등 외부 데이터베이스)을 활용한 ADG 정의와 실제 유전자 발현 데이터의 직접 분석을 결합하여, GeneDisco/DiscoBAX의 순수 데이터 기반 접근보다 생물학적 맥락 반영

- **행동 메모리의 다단계 추론**: 단순 이전 결과 누적이 아닌 각 행동-결과 쌍을 명시적으로 저장하여 에이전트가 이전 분석 결과를 기반으로 반사적 사고(reflection)를 수행할 수 있도록 지원

## Limitation & Further Study

- **데이터 접근성 제약**: 실제 실험실 환경에서 "각 라운드 후 즉시 섭동 결과 수신"이라는 가정이 실제 turnaround time, 비용 등으로 인해 제약될 수 있으며, 다중 라운드 동시 설계(parallel design) 시 성능 미검증

- **ADG(Associated Descriptive Genes) 정의의 주관성**: 사용자가 페놀타입 관련 유전자를 수동으로 정의해야 하는데, 이 초기 정의의 정확성이 에이전트 성능에 미치는 영향을 정량적으로 분석하지 않음. 자동 ADG 도출 메커니즘 필요

- **모델 크기와 비용의 trade-off**: 더 큰 LLM(GPT-4)이 성능이 우수하지만 API 비용, 응답시간, 프라이버시 이슈 미분석. 소규모 바이오 연구실의 접근성 제한 가능성

- **Hit 정의의 엄격성**: z-score 임계값 기반 hit 정의가 고정되어 있어, 연속적 표현형(continuous phenotype)이나 복잡한 다중 표현형(multi-phenotype) 상황에 대한 확장성 부족

- **후속 연구 방향**:
  - 실제 wet-lab 파이프라인과의 통합 검증 및 실험 시간-비용 최적화 분석
  - 자동 ADG 도출 또는 사용자 피드백 기반 ADG 동적 갱신 메커니즘
  - 개방형 소형 언어모델을 통한 온프레미스(on-premises) 배포 가능성 탐구
  - 다중 동시 라운드 설계, 비용-정확성 Pareto frontier 분석


## Evaluation

- Novelty: 4/5
- Technical Soundness: 4/5
- Significance: 4/5
- Clarity: 3.5/5
- Overall: 4/5

**총평**: PerTurboAgent는 자기-계획 LLM 에이전트를 통해 고비용 유전자 섭동 실험의 효율화라는 현실적 문제를 창의적으로 해결하는 연구로, 기존 활성학습 방법들을 일관되게 능가하는 경험적 성과를 보입니다. 다만 ADG 정의의 자동화, 실제 실험실 환경 검증, 이론적 기초의 강화가 이루어진다면 훨씬 더 강력한 기여가 될 수 있을 것으로 판단됩니다.

## Related Papers

- 🔄 다른 접근: [[papers/505_Llm4grn_Discovering_causal_gene_regulatory_networks_with_llm/review]] — 유전자 관련 실험에서 LLM을 활용한다는 공통점이 있지만 순차적 섭동 실험 설계와 조절 네트워크 발견이라는 다른 목적을 가진다.
- 🧪 응용 사례: [[papers/474_Large_language_models_for_zero-shot_inference_of_causal_stru/review]] — 생물학적 인과관계 추론 능력을 유전자 섭동 실험의 순차적 선택 최적화에 활용할 수 있다.
- 🔗 후속 연구: [[papers/239_CRISPR-GPT_for_agentic_automation_of_gene-editing_experiment/review]] — 유전자 편집 실험 자동화를 위한 CRISPR-GPT 기술을 유전자 섭동 실험 설계에 확장 적용할 수 있다.
- 🧪 응용 사례: [[papers/048_Adaptive_ai_decision_interface_for_autonomous_electronic_mat/review]] — 순차적 섭동 부스팅을 위한 자기 계획 에이전트의 구체적인 응용을 보여준다.
- 🧪 응용 사례: [[papers/474_Large_language_models_for_zero-shot_inference_of_causal_stru/review]] — 유전자 섭동 실험 설계에 인과관계 추론 능력을 활용하여 더 효과적인 실험 계획을 수립할 수 있다.
- 🔄 다른 접근: [[papers/505_Llm4grn_Discovering_causal_gene_regulatory_networks_with_llm/review]] — 유전자 섭동 실험에서 LLM을 활용한다는 공통점이 있지만 네트워크 발견과 실험 설계라는 다른 목적을 가진다.
