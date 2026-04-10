---
title: "724_SciHorizon_Benchmarking_AI-for-Science_Readiness_from_Scient"
authors:
  - "Chuan Qin"
  - "Xin Chen"
  - "Chengrui Wang"
  - "Pengmin Wu"
  - "Xi Chen"
date: "2025.03"
doi: "10.48550/arXiv.2503.13503"
arxiv: ""
score: 3.8
essence: "과학 AI(AI4Science)의 준비 상태를 평가하기 위한 통합 벤치마킹 프레임워크로, 과학 데이터의 AI 준비도와 대규모 언어모델(LLM)의 과학 분야별 능력을 체계적으로 평가하는 종합 평가 체계를 제시한다."
tags:
  - "cat/Academic_Peer_Review_Automation"
  - "sub/AI_Publishing_Trends"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qin et al._2025_SciHorizon Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models.pdf"
---

# SciHorizon: Benchmarking AI-for-Science Readiness from Scientific Data to Large Language Models

> **저자**: Chuan Qin, Xin Chen, Chengrui Wang, Pengmin Wu, Xi Chen, Yihang Cheng, Jingyi Zhao, Meng Xiao, Xiangchao Dong, Qingqing Long, Boya Pan, Han Wu, Chengzan Li, Yuanchun Zhou, Hui Xiong, Hengshu Zhu | **날짜**: 2025-03-12 | **DOI**: [10.48550/arXiv.2503.13503](https://doi.org/10.48550/arXiv.2503.13503)

---

## Essence

과학 AI(AI4Science)의 준비 상태를 평가하기 위한 통합 벤치마킹 프레임워크로, 과학 데이터의 AI 준비도와 대규모 언어모델(LLM)의 과학 분야별 능력을 체계적으로 평가하는 종합 평가 체계를 제시한다.

## Motivation

- **Known**: DeepMind의 AlphaFold, ChatGPT 등 AI 기술이 과학 분야에서 혁신적 성과를 내고 있으며, 다양한 LLM 벤치마크 프레임워크가 존재함

- **Gap**: ① AI 연구자들이 대규모 도메인 특화 데이터세트에서 가치 있는 통찰을 효율적으로 추출하지 못하고 있음 ② 기존 과학 데이터 평가 도구들은 AI 애플리케이션의 고유한 요구사항을 충분히 다루지 못함 ③ 기존 LLM 벤치마크는 특정 분야에 국한되어 있고 과학적 가치(scientific values)를 평가하지 않음

- **Why**: 고품질의 AI-준비 데이터(AI-ready data)의 부족과 과학 응용을 위한 종합적이고 미세한 수준의 LLM 평가 체계의 부재가 AI4Science 발전을 저해

- **Approach**: 과학 데이터 평가와 LLM 평가 두 관점에서 통합 프레임워크 제시

## Achievement

![Figure 1: SciHorizon 플랫폼 개요. 과학 데이터 평가, LLM 평가, 통합 플랫폼 구성](fig1)

1. **포괄적 데이터 AI-준비도 평가 프레임워크**: Quality(완전성, 정확성, 일관성, 적시성), FAIRness(발견가능성, 접근성, 상호운용성, 재사용성), Explainability(다양성, 편향성 제거, 도메인 적용성, 과제 적용성), Compliance(출처, 윤리성, 안전성, 신뢰성) 등 4개 주요 차원과 15개 세부 차원으로 구성

2. **멀티 분야 LLM 능력 평가**: 수학, 물리, 화학, 생명과학, 지구우주과학을 포괄하여 Knowledge(지식), Understanding(이해), Reasoning(추론), Multimodality(다중성식), Values(과학적 가치) 등 5개 핵심 지표로 16개 평가 차원 구성

3. **실증 평가**: 2018-2023년 peer-reviewed 저널의 약 1,500개 데이터세트를 분석하여 지구과학과 생명과학 AI-준비 데이터 추천 목록 제시, 20개 이상의 개방형/폐쇄형 LLM 종합 평가 수행

## How

![Figure: SciHorizon 프레임워크의 이중 평가 구조](fig_structure)

**데이터 평가 방법론**:
- 정성적(qualitative) 및 정량적(quantitative) 평가 통합
- 사전 훈련된 전문가 모델을 통한 자동 사전 스크리닝
- 10명의 도메인 전문가로 구성된 Delphi 방식 반복 검토로 합의 도출
- 계산 가능한 파라미터와 역사적 전문가 지식 기반 모델 추론값 결합

**LLM 평가 방법론**:
- 학문 분야별 맞춤형 벤치마크 데이터세트 개발
- 5개 핵심 역량 지표에 따른 다층적 성능 평가
- 단순 사실 회상(factual recall)을 넘어 과학 문제 해결 능력의 미세한 평가

**평가 대상**:
- 데이터: 1,500개 과학 데이터세트 (2018-2023)
- LLM: 20개 이상의 개방형(GPT-2, Llama 등) 및 폐쇄형(GPT-4, Claude 등) 모델

## Originality

- **통합적 관점**: 기존 연구들이 데이터 또는 LLM을 개별적으로 평가한 반면, SciHorizon은 AI4Science 생태계 전체를 종합적으로 평가하는 최초의 프레임워크 제시

- **도메인 특화 설계**: 일반적 데이터 준비도 평가와 달리 과학 데이터의 고유한 특성(재현성, 메타데이터 완전성, 시간적 진화 등)을 고려한 맞춤형 평가 체계

- **과학적 가치 평가**: LLM 벤치마킹에서 학술 무결성, 공정성, 투명성 등 과학 연구 가치를 처음으로 체계적으로 평가

- **실제 데이터 기반**: 1,500개 실제 과학 데이터 자원 논문 분석을 통한 현실성 있는 추천 목록 제시

- **개방형 플랫폼**: 모든 평가 결과의 공개 온라인 제공 (www.scihorizon.cn/en)으로 커뮤니티 공헌

## Limitation & Further Study

- **데이터 분석의 한계**: 약 1,500개 데이터세트 분석이 전체 과학 데이터를 대표하기에 충분한지 불명확하며, 2018-2023 기간에 제한됨으로 인한 시간 편향 가능성

- **전문가 평가의 주관성**: Delphi 프로세스의 합의 도출에 참여한 10명 전문가의 선정 기준과 그들의 도메인 편향이 명확히 제시되지 않음

- **LLM 평가의 동적 특성**: 급속히 발전하는 LLM 환경에서 평가 결과의 장기적 유효성이 제한적이며, 지속적 업데이트 메커니즘이 필요

- **학제간 평가 깊이**: 5개 과학 분야를 포괄하면서도 각 분야별 심화 평가 수준이 균등한지 불분명

- **후속 연구 방향**:
  - 시계열 평가를 통한 데이터와 LLM 성능의 동적 변화 추적
  - 평가 기준의 자동화 및 AI 기반 평가 도구 개발
  - 특정 과학 응용(단백질 구조 예측, 신약 개발 등)에 대한 심화 평가
  - 개발도상국 과학 데이터의 포함 확대

## Evaluation

- **Novelty**: 4.5/5 - 데이터와 LLM을 통합적으로 평가하고 과학적 가치를 포함한 점은 매우 참신하나, 개별 평가 차원들은 기존 개념의 조합

- **Technical Soundness**: 3.5/5 - Delphi 프로세스 등 평가 방법론은 타당하나, 전문가 선정 기준, 가중치 설정, 자동화 메커니즘에 대한 상세 설명 부족

- **Significance**: 4/5 - AI4Science 커뮤니티에 실질적 의사결정 도구 제공 및 데이터-모델 간극 파악에 높은 가치를 가지나, 실제 과학 혁신으로의 영향은 추적 필요

- **Clarity**: 3.5/5 - 전체 구조와 동기는 명확하나, 본문 초반의 15개 세부 차원과 16개 평가 차원에 대한 상세한 정의와 구체적 평가 사례 부족

- **Overall**: 3.8/5

**총평**: SciHorizon은 AI4Science의 현재 준비 상태를 진단하기 위한 야심찬 통합 프레임워크로, 특히 과학적 가치 평가와 공개 플랫폼 제공을 통해 학계에 의미 있는 기여를 하고 있다. 다만 평가 방법론의 자동화, 전문가 편향 제어, 시간에 따른 동적 업데이트 메커니즘 강화가 필요하며, 프레임워크의 장기적 유효성 검증을 위한 후속 연구가 지속되어야 한다.

## Related Papers

- 🏛 기반 연구: [[papers/090_AIRS-Bench_a_Suite_of_Tasks_for_Frontier_AI_Research_Science/review]] — 프론티어 AI 연구 과학을 위한 작업 모음이 SciHorizon의 평가 체계 설계에 기반을 제공한다.
- 🔄 다른 접근: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — 과학적 발견에서 LLM 벤치마킹의 다른 접근 방식을 제시한다.
- 🔗 후속 연구: [[papers/713_Scicueval_A_comprehensive_dataset_for_evaluating_scientific/review]] — 과학적 이해 평가를 위한 포괄적 데이터셋이 SciHorizon의 평가 범위를 확장한다.
- 🧪 응용 사례: [[papers/716_ScienceAgentBench_Toward_Rigorous_Assessment_of_Language_Age/review]] — 언어 에이전트의 엄격한 평가가 SciHorizon의 AI 준비도 측정에 적용된다.
- 🔄 다른 접근: [[papers/669_Researchbench_Benchmarking_llms_in_scientific_discovery_via/review]] — SciHorizon의 과학 준비도 벤치마킹과 ResearchBench는 AI의 과학적 역량을 서로 다른 관점에서 평가하는 보완적 접근법입니다
- 🔄 다른 접근: [[papers/261_Deepresearch_bench_A_comprehensive_benchmark_for_deep_resear/review]] — 과학 준비성 벤치마킹과 깊이 있는 연구 에이전트 평가의 다른 접근법
