---
title: "362_From_LLMs_to_LLM-based_Agents_for_Software_Engineering_A_Sur"
authors:
  - "Haolin Jin"
  - "Linghan Huang"
  - "Haipeng Cai"
  - "Jun Yan"
  - "Bo Li"
date: "2024"
doi: "10.48550/arXiv.2408.02479"
arxiv: ""
score: 4.3
essence: "본 논문은 소프트웨어 공학(SE) 분야에서 대규모 언어 모델(LLM)과 LLM 기반 에이전트의 현황을 구분하여 체계적으로 분석하는 첫 번째 포괄적 조사이다. 요구사항 공학, 코드 생성, 자율적 의사결정, 소프트웨어 설계, 테스트 생성, 소프트웨어 보안 및 유지보수의 6가지 핵심 영역에서 139개 논문을 수집하여 LLM과 LLM 기반 에이전트의 차이점을 명확히 한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Specialized_Domain_Agents"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Jin et al._2024_From LLMs to LLM-based Agents for Software Engineering A Survey of Current, Challenges and Future.pdf"
---

# From LLMs to LLM-based Agents for Software Engineering: A Survey of Current, Challenges and Future

> **저자**: Haolin Jin, Linghan Huang, Haipeng Cai, Jun Yan, Bo Li | **날짜**: 2024 | **DOI**: [10.48550/arXiv.2408.02479](https://doi.org/10.48550/arXiv.2408.02479)

---

## Essence

![Figure 1](figures/fig1.webp) *2020-2024년 LLM 및 LLM 기반 에이전트 논문 추이*

본 논문은 소프트웨어 공학(SE) 분야에서 대규모 언어 모델(LLM)과 LLM 기반 에이전트의 현황을 구분하여 체계적으로 분석하는 첫 번째 포괄적 조사이다. 요구사항 공학, 코드 생성, 자율적 의사결정, 소프트웨어 설계, 테스트 생성, 소프트웨어 보안 및 유지보수의 6가지 핵심 영역에서 139개 논문을 수집하여 LLM과 LLM 기반 에이전트의 차이점을 명확히 한다.

## Motivation

- **Known**: 최근 LLM(GPT, Codex 등)은 코드 생성, 버그 수정, 문서화 등 소프트웨어 공학 작업에서 놀라운 성능을 보였으며, 기존 신경망 기반 접근법의 특성 공학(feature engineering) 및 확장성 문제를 해결함

- **Gap**: 기존 조사 논문들(Fan et al. 2023 등)은 LLM의 적용에 중점을 두었으나, 새롭게 등장한 **LLM 기반 에이전트와의 명확한 구분이 부족**하고, 요구사항 공학 등 상위 수준의 소프트웨어 공학 작업에 대한 커버리지가 불충분함

- **Why**: LLM은 문맥 길이 제한, 할루시네이션(hallucination), 외부 도구 활용 불가, 정적 특성 등 심각한 한계를 가지고 있으나, LLM 기반 에이전트는 RAG(Retrieval-Augmented Generation), 도구 통합, 자율적 의사결정을 통해 이러한 문제를 극복할 수 있음

- **Approach**: 6가지 소프트웨어 공학 영역에서 LLM과 LLM 기반 에이전트의 작업, 벤치마크, 평가 지표를 비교 분석하고, 사용된 모델과 벤치마크를 종합적으로 검토

## Achievement

![Figure 2](figures/fig2.webp) *소프트웨어 공학 영역별 논문 분포*

1. **LLM과 LLM 기반 에이전트의 명확한 구분**: 
   - LLM: 고정된 학습 데이터에 기반한 정적 생성 모델
   - LLM 기반 에이전트: 외부 도구, RAG, 자율적 의사결정 능력을 갖춘 동적 시스템으로 AGI(인공일반지능)에 더 가까운 특성 보유

2. **6개 SE 영역에 대한 포괄적 분석**:
   - 요구사항 공학 및 문서화 (28건)
   - 코드 생성 및 소프트웨어 개발 (35건)
   - 자율적 학습 및 의사결정 (30건)
   - 소프트웨어 설계 및 평가 (19건)
   - 소프트웨어 테스트 생성 (15건)
   - 소프트웨어 보안 및 유지보수 (43건)
   총 139개 논문 체계화

3. **최신 연구 동향 반영**: 2023년 하반기부터 2024년 12월까지의 최신 논문을 중심으로 LLM 기반 에이전트 논문이 급격히 증가 추세를 정량적으로 제시 (2023년 1건→2024년 42건)

## How

- **연구 수집 방법론**: DBLP와 arXiv에서 2023년 하반기부터 2024년 12월까지 관련 논문 수집하여 중복을 제거한 후 6개 SE 영역으로 분류

- **비교 분석 프레임워크**:
  - 각 영역별로 LLM과 LLM 기반 에이전트가 수행하는 구체적 작업 열거
  - 사용된 벤치마크 데이터셋 및 평가 지표 비교
  - 자율성, 동적 적응성, 외부 도구 활용 여부에 따른 구분

- **4가지 핵심 연구 질문(RQ) 설정**:
  - RQ1: 최첨단 기법 및 관행 현황
  - RQ2: LLM과 LLM 기반 에이전트의 작업 성능 차이
  - RQ3: 가장 많이 사용되는 벤치마크 및 평가 지표
  - RQ4: SE에서 주로 사용되는 LLM 모델

- **기존 조사와의 차별화**: 이전 조사(Fan et al., Qian et al.)와 달리 LLM 기반 에이전트를 명확히 구분하고, 요구사항 공학의 최근 발전을 강조하며, 더 최신의 시간 범위(2023년 후반~2024년) 커버

## Originality

- **첫 번째 포괄적 비교 분석**: 기존 조사가 LLM 중심이었다면, 본 논문은 LLM 기반 에이전트라는 새로운 패러다임을 명확히 정의하고 체계적으로 비교하는 첫 시도

- **6개 SE 영역의 균형잡힌 커버리지**: 기존 조사가 코드 생성과 버그 수정에 편향되었던 반면, 요구사항 공학(28건), 설계(19건) 등 상위 수준의 작업도 동등하게 포함

- **LLM-기반 에이전트의 기술적 정의**: WS(World Scope) 프레임워크를 활용하여 LLM 기반 에이전트가 NLP에서 AGI로의 진전 중 3-4단계를 달성할 수 있음을 체계화

- **시의성**: 2023년 LLM 기반 에이전트 연구 급증(1건→42건)이라는 현상을 정량적으로 포착하여 새로운 연구 방향 제시

## Limitation & Further Study

- **벤치마크 표준화 부재**: LLM 기반 에이전트가 아직 초기 단계이며 통일된 벤치마크 및 정성적 기준이 부족하여, 어떤 솔루션을 LLM 기반 에이전트로 정의할 것인지 학계적 합의가 필요

- **평가 지표의 불일치**: 6개 SE 영역에서 사용되는 평가 지표가 다양하고 표준화되지 않아 크로스 도메인 비교의 어려움

- **실제 프로덕션 환경 검증 부족**: 대부분의 논문이 제한된 데이터셋과 작은 규모 프로젝트에서 평가되었으며, 대규모 실무 프로젝트에서의 검증 필요

- **후속 연구 방향**:
  - LLM 기반 에이전트의 정식화(formalization)와 표준화된 벤치마크 개발
  - 자율적 의사결정과 자기 개선 메커니즘의 심화 연구
  - 보안 취약점 및 할루시네이션 문제 해결
  - 마이크로서비스, 클라우드 네이티브 등 현대적 아키텍처에 대한 적용성 확대


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.3/5

**총평**: 본 논문은 LLM과 LLM 기반 에이전트를 명확히 구분한 첫 번째 포괄적 조사로서, 빠르게 진화하는 AI 기반 소프트웨어 공학 분야에서 시의성 높은 기여를 제공한다. 다만 벤치마크 표준화 부재와 실무 검증 부족이 한계이며, 후속 연구가 이러한 격차를 메우기를 기대한다.

## Related Papers

- 🏛 기반 연구: [[papers/586_Opendevin_An_open_platform_for_ai_software_developers_as_gen/review]] — LLM 기반 소프트웨어 엔지니어링 에이전트 연구의 포괄적 이론적 배경을 제공한다.
