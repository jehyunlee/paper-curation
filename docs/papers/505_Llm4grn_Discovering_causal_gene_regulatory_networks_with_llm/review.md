---
title: "505_Llm4grn_Discovering_causal_gene_regulatory_networks_with_llm"
authors:
  - "Tejumade Afonja"
  - "Ivaxi Sheth"
  - "Ruta Binkyte"
  - "Waqar Hanif"
  - "Thomas Ulas"
date: "2024"
doi: "arXiv:2410.15828"
arxiv: ""
score: 4.0
essence: "본 논문은 단일세포 RNA 시퀀싱(scRNA-seq) 데이터에서 유전자 조절 네트워크(Gene Regulatory Network, GRN)를 발견하기 위해 대규모 언어모델(LLM)을 활용하는 새로운 접근 방식을 제시합니다. 신뢰할 수 있는 정답 그래프가 없는 상황에서 인과관계 합성 데이터 생성을 평가 방법으로 사용하여 LLM의 효과성을 입증합니다."
tags:
  - "cat/AI-Driven_Materials_and_Drug_Discovery"
  - "sub/Biomedical_Causal_Modeling"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Bo et al._2024_Llm4grn Discovering causal gene regulatory networks with llms–evaluation through synthetic data gen.pdf"
---

# LLM4GRN: Discovering causal gene regulatory networks with llms–evaluation through synthetic data generation

> **저자**: Tejumade Afonja, Ivaxi Sheth, Ruta Binkyte, Waqar Hanif, Thomas Ulas, Matthias Becker, Mario Fritz | **날짜**: 2024 | **DOI**: [arXiv:2410.15828](https://arxiv.org/abs/2410.15828)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: LLM4GRN 개요. Setting 1.A는 인간 기반 지식베이스(KB)와 LLM을 결합하고, Setting 2.A는 LLM KB와 LLM 추론을 모두 활용하는 완전 LLM 파이프라인*

본 논문은 단일세포 RNA 시퀀싱(scRNA-seq) 데이터에서 유전자 조절 네트워크(Gene Regulatory Network, GRN)를 발견하기 위해 대규모 언어모델(LLM)을 활용하는 새로운 접근 방식을 제시합니다. 신뢰할 수 있는 정답 그래프가 없는 상황에서 인과관계 합성 데이터 생성을 평가 방법으로 사용하여 LLM의 효과성을 입증합니다.

## Motivation

- **Known**: 통계적 인과 발견 알고리즘(causal discovery algorithms)은 기존에 GRN 추론에 사용되어 왔으나, 고차원의 노이즈가 많은 단일세포 데이터에서 허위 상관관계를 감지하기 쉽고 강건성이 떨어짐. 또한 TRANSFAC, RegNetwork 등의 사전 학습된 데이터베이스는 세포 유형이나 조건별 맥락 정보 부족

- **Gap**: 기존 방법들은 인과 구조를 발견하는 데 필요한 다양한 생물학적 지식을 효과적으로 통합하지 못하며, GRN 추론을 위해 일반 목적의 LLM을 활용한 연구가 부재

- **Why**: LLM은 광범위한 과학 문헌과 생물학적 데이터베이스로부터 학습한 맥락 정보를 활용하여 복잡한 생물학적 상호작용을 포착할 수 있는 강력한 도구

- **Approach**: (1) LLM을 통해 직접 완전한 GRN을 생성하거나, (2) 잠재적 전사인자(TF) 목록 형태의 사전 지식을 제공하여 통계적 인과 발견 알고리즘과 결합. 신뢰할 수 있는 정답 그래프 대신 인과관계 합성 데이터 생성을 평가 작업으로 활용하여 통계적/생물학적 타당성 검증

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 다양한 방법들이 제안하는 GRN 간의 겹침(overlap) 분석. LLM이 더 높은 겹침을 시연*

1. **LLM의 효과성 입증**: 일반 목적의 LLM이 복잡한 생물학적 상호작용을 포착하여 GRN 추론에 효과적임을 시연. GPT-4 등의 모델이 생물학적 지식을 통합하여 합리적인 GRN 그래프를 제안

2. **통계적/생물학적 평가 프레임워크**: 인과관계 합성 데이터 생성을 통한 신규 평가 방법론. 정답 그래프가 부재한 상황에서 GRouNdGAN을 활용하여 합성 데이터와 원본 데이터의 통계적 유사성과 생물학적 타당성을 비교 검증

3. **하이브리드 접근의 우수성**: LLM과 통계적 방법(GRNBoost2)의 결합이 단독 사용보다 우수한 성능을 달성. LLM의 광범위한 지식과 통계적 방법의 데이터 기반 접근이 상호 보완

## How

![Figure 3](figures/fig3.webp)
*그림 3: 서로 다른 세포 유형에 걸친 상위 마커 유전자들의 유전자 발현 프로필을 보여주는 점 플롯*

- **Setting 1 (인간 KB 기반)**: 
  - 1.A: 인간 큐레이션 데이터베이스에서 제공한 TF 후보 목록을 LLM에 제공하여 GRN 그래프 추론
  - 1.B: 동일한 TF 목록을 GRNBoost2(통계적 방법)에 입력하여 비교 기준으로 사용

- **Setting 2 (LLM KB 기반)**:
  - 2.A: LLM 자체를 지식베이스로 활용하여 잠재적 TF 추론과 GRN 그래프 생성을 모두 수행
  - 2.B: LLM에서 추출한 TF 목록을 GRNBoost2에 입력

- **평가 파이프라인**:
  - 추론된 GRN 그래프를 GRouNdGAN(인과 GAN)에 입력
  - GRN을 반영한 합성 scRNA-seq 데이터 생성
  - 합성 데이터와 원본 데이터의 비교: (a) 통계적 유사성(분포, 상관성), (b) 생물학적 타당성(세포 유형 비율, 마커 유전자 발현)

- **LLM 쿼리 전략**:
  - 구조화된 프롬프트를 통해 LLM에 PBMC(말초혈액 단핵세포) 데이터에서 관련 전사인자와 그들의 표적 유전자 관계를 요청
  - 다중 LLM(GPT-4, Llama 등)에 대해 비교 평가

## Originality

- **첫 번째 일반 목적 LLM의 GRN 추론 적용**: 기존 연구는 LLM을 통계적 방법 정제에만 사용했으나, 본 연구는 LLM을 주요 추론 도구로 활용

- **신규 평가 방법론의 제시**: 정답 그래프 부재 문제를 해결하기 위해 인과관계 합성 데이터 생성을 평가 작업으로 도입. 기존 인과 벤치마크 데이터셋의 학습 데이터 오염(training data contamination) 문제를 회피

- **다층적 평가 프레임워크**: 통계적 메트릭(분포 유사성, 상관계수) 뿐만 아니라 생물학적 타당성(세포 유형 분석, 마커 유전자 발현 패턴)을 동시에 평가하여 실제 생물학적 의미를 검증

- **체계적 비교 분석**: 인간 KB vs LLM KB, LLM 그래프 vs 통계적 그래프 등 네 가지 설정에서 포괄적 비교를 통해 각 접근의 장단점 명시

## Limitation & Further Study

- **LLM의 환각(hallucination) 문제**: LLM이 생성한 TF-유전자 상호작용이 실제 생물학적 근거 없이 그럴듯하게 보일 수 있음. 생성된 상호작용에 대한 문헌 검증이나 실험적 검증 부재

- **제한된 데이터셋**: PBMC-All 데이터셋 중심의 평가로 다양한 세포 유형과 조건에 대한 일반화 능력 불명확. 다른 조직/질병 상태의 scRNA-seq 데이터에 대한 검증 필요

- **정답 그래프 부재로 인한 평가의 한계**: 합성 데이터 생성 기반 평가는 간접적 평가이며, 실제 인과관계를 완벽히 검증할 수 없음. 생물학적으로 검증된 GRN과의 직접 비교 불가능

- **LLM 크기와 성능의 관계 미분석**: 모델 크기, 학습 데이터, 파라미터 수 등이 GRN 추론 성능에 미치는 영향에 대한 체계적 분석 부재

- **계산 비용과 실용성**: LLM 기반 접근의 계산 비용, 지연시간, 확장성에 대한 논의 부족. 대규모 유전자 세트에 대한 적용 가능성 불명확

- **후속 연구 방향**:
  - 생물학적으로 검증된 GRN 데이터베이스를 구축하여 직접 평가 가능한 벤치마크 개발
  - 다양한 세포 유형, 질병 상태, 조직별 확대 평가
  - LLM의 환각을 최소화하기 위한 프롬프트 최적화 및 검증 메커니즘 개발
  - 실제 CRISPR 스크리닝 실험 데이터와의 비교 검증
  - 하이브리드 모델의 최적 구조 및 파라미터 튜닝 방법론 개발

## Evaluation

- **Novelty**: 4/5 
  - LLM을 GRN 추론의 주요 도구로 활용하고, 합성 데이터 생성 기반의 신규 평가 방법론 제시
  - 다만 LLM 기반 인과 발견 일반 연구는 이미 존재하며, GRN 특화성은 중등도

- **Technical Soundness**: 4/5
  - 방법론적으로 타당하며, GRouNdGAN을 활용한 합성 데이터 생성과 다층 평가가 체계적
  - 다만 정답 그래프 부재로 인한 평가의 간접성, LLM 환각 문제에 대한 제한적 논의

- **Significance**: 3.5/5
  - 실제 생물학적 발견으로 이어질 가능성이 있으나, 현재로서는 개념 검증(proof-of-concept) 수준
  - 단일 데이터셋(PBMC) 중심의 평가로 일반화 가능성 불명확
  - 생물학적 검증과 실용적 적용 사이의 간극 존재

- **Clarity**: 4/5
  - 전반적으로 잘 구성되었으나, LLM 프롬프팅 구체 내용과 하이퍼파라미터 설정에 대한 상세 기술 부족
  - Figure와 설명이 대체로 명확하나, 통계적 메트릭의 상세 정의 필요

- **Overall**: 4/5

**총평**: 본 논문은 일반 목적 LLM을 GRN 추론에 처음 적용하고, 신규 평가 방법론을 제시하여 LLM과 통계적 방법의 하이브리드 접근이 실질적 가치를 가짐을 보여줍니다. 다만 단일 데이터셋 평가, 간접적 평가 방법론, LLM 환각 문제 등으로 인해 생물학적 발견으로의 직접적 전환에는 추가 검증이 필요합니다. scRNA-seq 분석에 AI를 활용하는 분야에서 의미 있는 기여이나, 기초 생물학 연구의 실제 문제 해결 수준까지는 도달하지 못한 상태입니다.

## Related Papers

- 🏛 기반 연구: [[papers/474_Large_language_models_for_zero-shot_inference_of_causal_stru/review]] — 생물학적 인과관계 추론의 일반적 프레임워크를 유전자 조절 네트워크 발견이라는 구체적 문제에 적용한다.
- 🔄 다른 접근: [[papers/615_PerTurboAgent_A_Self-Planning_Agent_for_Boosting_Sequential/review]] — 유전자 섭동 실험에서 LLM을 활용한다는 공통점이 있지만 네트워크 발견과 실험 설계라는 다른 목적을 가진다.
- 🔗 후속 연구: [[papers/371_GeneAgent_self-verification_language_agent_for_gene-set_anal/review]] — 유전자 집합 분석을 위한 자기 검증 언어 에이전트 기술을 유전자 조절 네트워크 분석에 확장할 수 있다.
- 🔗 후속 연구: [[papers/474_Large_language_models_for_zero-shot_inference_of_causal_stru/review]] — 유전자 조절 네트워크 발견을 위한 LLM 활용 연구로, 생물학적 인과관계 추론의 구체적 적용 사례이다.
- 🔄 다른 접근: [[papers/615_PerTurboAgent_A_Self-Planning_Agent_for_Boosting_Sequential/review]] — 유전자 관련 실험에서 LLM을 활용한다는 공통점이 있지만 순차적 섭동 실험 설계와 조절 네트워크 발견이라는 다른 목적을 가진다.
