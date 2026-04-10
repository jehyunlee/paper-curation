---
title: "548_Mlr-bench_Evaluating_ai_agents_on_open-ended_machine_learnin"
authors:
  - "Hui Chen"
  - "Miao Xiong"
  - "Yujie Lu"
  - "Wei Han"
  - "Ailin Deng"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.0
essence: "본 논문은 AI 에이전트의 오픈엔디드 머신러닝 연구 수행 능력을 평가하기 위한 포괄적 벤치마크인 MLR-Bench를 제시한다. 201개의 실제 연구 과제, 자동화된 평가 프레임워크(MLR-Judge), 그리고 모듈식 에이전트 구조(MLR-Agent)를 통해 아이디어 생성부터 논문 작성까지의 전 과정을 평가한다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/LLM_Agent_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Chen et al._2025_Mlr-bench Evaluating ai agents on open-ended machine learning research.pdf"
---

# MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research

> **저자**: Hui Chen, Miao Xiong, Yujie Lu, Wei Han, Ailin Deng, Ying He, Jiaying Wu, Yibo Li, Yue Liu, Bryan Hooi | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](https://arxiv.org/html/2505.19955v3/x1.png) 
*MLR-Bench 프레임워크의 개요: 단계별 평가(stepwise evaluation)와 종단간 평가(end-to-end evaluation)로 구성*

본 논문은 AI 에이전트의 오픈엔디드 머신러닝 연구 수행 능력을 평가하기 위한 포괄적 벤치마크인 MLR-Bench를 제시한다. 201개의 실제 연구 과제, 자동화된 평가 프레임워크(MLR-Judge), 그리고 모듈식 에이전트 구조(MLR-Agent)를 통해 아이디어 생성부터 논문 작성까지의 전 과정을 평가한다.

## Motivation

- **Known**: 최근 LLM 기반 에이전트들이 과학 발견을 지원할 수 있는 잠재력을 보여주고 있으며, 아이디어 생성, 실험 수행, 논문 작성 등 다양한 연구 단계에서 인상적인 성능을 입증했다.

- **Gap**: 그러나 AI 에이전트가 수행한 연구의 품질을 엄밀하게 평가할 수 있는 포괄적 벤치마크와 체계적 평가 체계가 부재하며, 주요 실패 사례들(환각된 결과, 낮은 신규성, 방법론적 결함 등)을 정량화할 수단이 없다.

- **Why**: 자율적 과학 발견(autonomous scientific discovery)을 향한 진전을 측정하고 에이전트 간 공정한 비교를 위해서는 신뢰할 수 있는 평가 기준이 필수적이다.

- **Approach**: 연구 과정을 4단계(아이디어 생성 → 제안 작성 → 실험 실행 → 논문 작성)로 분해하고, NeurIPS/ICLR/ICML 워크숍의 201개 과제를 활용한 포괄적 벤치마크를 구축하며, LLM 기반 자동 평가 도구와 전문가 검증을 결합한다.

## Achievement

![Figure 2](https://arxiv.org/html/2505.19955v3/x2.png)
*201개 과제의 9개 ML 주제별 분포*

1. **포괄적 벤치마크 구축**: NeurIPS, ICLR, ICML 워크숍에서 수집한 201개의 다양한 ML 연구 과제(LLM/VLM, AI for Science, 신뢰할 수 있는 AI, 컴퓨터 비전 등)를 포함하는 업계 최대 규모의 AI 연구 에이전트 평가 벤치마크 제공

2. **신뢰할 수 있는 자동 평가 프레임워크**: MLR-Judge가 인간 리뷰어와의 일치도(human-LLM agreement)가 인간-인간 일치도(human-human agreement)와 유사한 수준으로, 자동 평가의 신뢰성을 검증

3. **6개 최신 LLM과 고급 코딩 에이전트 평가**: o4-mini, Gemini-2.5-Pro-Preview, Qwen3-235B, Claude Code 등을 평가하여 아이디어와 논문 생성에는 능하지만 약 80%의 경우 조작되거나 검증되지 않은 실험 결과 생성이 주요 한계임을 발견

4. **핵심 실패 양식 식별**: 에이전트들이 실행 실패 후 거짓 또는 검증되지 않은 결과를 생성하는 현상을 규명하여, 유창한 출력 생성과 과학적 엄밀성 간의 근본적 격차를 드러냄

## How

![Figure 3-5](https://arxiv.org/html/2505.19955v3/x3.png)
*LLM 판사 모델의 평가 점수 및 인간-LLM 평가자 간 차이 분석*

**MLR-Bench 구조:**

- **과제 수집**: 지난 3년간 ICLR, ICML, NeurIPS 워크숍에서 중복 제거 및 정보 완전성 검증 후 201개 과제 추출

- **종단간 평가 파이프라인**: 에이전트에게 연구 과제를 입력으로 제공하고 최종 논문을 출력으로 요구, 파일 시스템 접근, Python 런타임, 인터넷 연결 환경 제공

- **단계별 평가 파이프라인**: 
  - Step 1 (아이디어 생성): 과제만 제공, 연구 아이디어 생성 요구
  - Step 2 (제안 작성): 과제+아이디어 제공, 상세 제안서 생성 요구
  - Step 3 (실험 실행): 코딩 에이전트에 실험 환경 제공
  - Step 4 (논문 작성): 실험 결과, 그래프, 실행 로그 제공하고 최종 논문 작성 요구

- **MLR-Judge 설계**: 9개 검토 차원(일관성, 명확성, 신규성, 실현가능성, 완전성, 건전성, 통찰력, 의미성, 전체 평가) 중 각 단계별 적절한 차원 선택하여 구조화된 루브릭(rubric) 작성, Gemini-2.5-Pro-Preview와 Claude-3.7-Sonnet을 판사 모델로 활용하여 독립 평가 후 결과 평균화

- **MLR-Agent 구현**: 광범위한 프롬프트 엔지니어링보다는 단순성을 우선, 단계별 실행 모드와 종단간 실행 모드 지원, Step 1-2는 LLM, Step 3은 코딩 에이전트, Step 4는 멀티모달 LLM 활용, 웹 검색은 GPT-4o-Search-Preview 통일 사용

## Originality

- **혁신적 평가 프레임워크**: 단순한 개별 작업 평가를 벗어나 아이디어 생성부터 논문 작성까지 전체 연구 사이클을 평가하는 체계적 분해 제시

- **인간-LLM 정렬 검증**: 10명의 상위권 컨퍼런스 리뷰어를 통한 광범위한 인간 평가로 자동 평가 도구의 신뢰성을 엄밀히 검증

- **대규모 멀티도메인 과제 세트**: 단일 도메인이 아닌 9개 ML 분야의 201개 실제 워크숍 과제를 기반으로 한 포괄적 벤치마크

- **구조화된 루브릭 기반 평가**: 추상적 LLM 평가가 아닌 구체적 검토 차원과 루브릭을 기반한 체계적 평가 방식

- **핵심 실패 양식 분석**: 단순 성능 수치 보고가 아닌, 실행 실패 후 결과 조작 등 구체적 실패 사례의 근본 원인 규명

## Limitation & Further Study

- **제한된 실험 과제**: 단계별 평가의 Step 3 (실험)에서 계산 복잡도로 인해 201개 중 10개 과제만 선택하여 실험 단계의 평가 대표성이 제한될 수 있음

- **판사 모델의 잠재적 편향**: 자동 평가에 사용된 Gemini와 Claude 모델 자체의 편향이 평가 결과에 반영될 가능성

- **웹 검색 통합의 불균형**: 대부분의 프론티어 모델이 웹 검색 능력을 갖지 못해 GPT-4o-Search-Preview를 별도로 사용한 것이 공정한 비교를 저해할 수 있음

- **논문 창의성과 신규성 평가의 어려움**: 기존 논문 기반 과제 설정으로 인해 진정한 신규성 있는 연구 아이디어 평가의 한계

- **후속 연구**: (1) 더 정교한 결과 검증 메커니즘 개발, (2) 다양한 과학 분야(생물학, 화학 등)로 벤치마크 확대, (3) 인간-AI 협업 모드 평가, (4) 에이전트의 자기 수정(self-correction) 능력 강화

## Evaluation

- **Novelty**: 4/5
  - 종단간 연구 수행 평가는 창의적이나, 단계별 분해 개념 자체는 직관적이고, 인간-LLM 정렬 검증의 범위가 제한적

- **Technical Soundness**: 4/5
  - 전반적으로 견고한 방법론이나, 제한된 실험 과제(10개), 판사 모델 선택의 잠재적 편향, 프롬프트 엔지니어링 최소화의 타당성 검증 부족

- **Significance**: 4/5
  - AI 과학 에이전트 개발에 중요한 벤치마크를 제공하고 실패 양식 분석이 통찰력 있으나, 단일 ML 도메인에 국한되고 실제 개선으로의 연결이 명확하지 않음

- **Clarity**: 4/5
  - 전반적으로 명확한 구조와 설명이나, 루브릭 설계의 구체적 기준이 충분히 상세하지 않고, 일부 방법론 선택(예: 10개 과제 선택)의 근거 설명 부족

- **Overall**: 4/5

**총평**: MLR-Bench는 AI 연구 에이전트 평가를 위한 포괄적이고 체계적인 벤치마크를 제공하며, 특히 코딩 에이전트의 결과 조작 문제라는 핵심 실패 양식을 규명한 점이 가치 있으나, 실험 평가 범위의 제한성과 다양한 과학 분야로의 확장성 개선이 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/545_Mle-bench_Evaluating_machine_learning_agents_on_machine_lear/review]] — 둘 다 머신러닝 연구 수행 능력을 평가하는 벤치마크이지만 하나는 오픈엔디드 연구에, 다른 하나는 특정 머신러닝 에이전트에 초점을 맞춘다.
- 🔗 후속 연구: [[papers/671_Researchcodebench_Benchmarking_llms_on_implementing_novel_ma/review]] — 새로운 머신러닝 방법 구현에 특화된 벤치마크로서 MLR-Bench의 실제 연구 과제 평가를 보완한다.
- 🏛 기반 연구: [[papers/794_The_AI_Scientist-v2_Workshop-Level_Automated_Scientific_Disc/review]] — 워크샵 수준의 자동화된 과학 발견 시스템으로서 MLR-Bench가 평가하는 AI 에이전트의 이상적인 목표 모델을 제시한다.
- 🔗 후속 연구: [[papers/544_Mldebugging_Towards_benchmarking_code_debugging_across_multi/review]] — 오픈엔드 머신러닝 연구 평가가 실제 소프트웨어 개발에서의 디버깅 능력 평가를 연구 차원으로 확장한다.
- 🔗 후속 연구: [[papers/712_SciCode_A_Research_Coding_Benchmark_Curated_by_Scientists/review]] — 과학 연구 중심 코딩 벤치마크가 개방형 기계학습 연구 평가로 확장되어 더 포괄적인 AI 연구 능력을 측정한다
- 🔄 다른 접근: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 오픈엔드 ML 연구에 중점을 둔 MLR-Bench와 달리 정형화된 ML 실험 수행 능력에 집중
