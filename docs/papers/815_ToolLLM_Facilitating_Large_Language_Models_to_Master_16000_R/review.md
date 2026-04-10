---
title: "815_ToolLLM_Facilitating_Large_Language_Models_to_Master_16000_R"
authors:
  - "Yujia Qin"
  - "Shihao Liang"
  - "Yining Ye"
  - "Kunlun Zhu"
  - "Lan Yan"
date: "2023.10"
doi: "10.48550/arXiv.2307.16789"
arxiv: ""
score: 4.2
essence: "오픈소스 LLM들의 API 활용 능력을 대폭 향상시키기 위해 16,464개의 실제 REST API를 포함한 대규모 도구 사용 지시튜닝 데이터셋(ToolBench)과 깊이 우선 탐색 기반 의사결정 트리(DFSDT) 알고리즘을 제시하며, ChatGPT와 비슷한 성능의 ToolLLaMA를 개발했다."
tags:
  - "cat/Scientific_Language_Processing_and_Visualization"
  - "sub/LLM_Agent_Benchmarking"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Qin et al._2023_ToolLLM Facilitating Large Language Models to Master 16000+ Real-world APIs.pdf"
---

# ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs

> **저자**: Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark Gerstein, Dahai Li, Zhiyuan Liu, Maosong Sun | **날짜**: 2023-10-03 | **DOI**: [10.48550/arXiv.2307.16789](https://doi.org/10.48550/arXiv.2307.16789)

---

## Essence

오픈소스 LLM들의 API 활용 능력을 대폭 향상시키기 위해 16,464개의 실제 REST API를 포함한 대규모 도구 사용 지시튜닝 데이터셋(ToolBench)과 깊이 우선 탐색 기반 의사결정 트리(DFSDT) 알고리즘을 제시하며, ChatGPT와 비슷한 성능의 ToolLLaMA를 개발했다.

## Motivation

- **Known**: ChatGPT와 GPT-4 같은 폐쇄형 LLM은 뛰어난 도구 활용 능력을 보유하고 있으나, LLaMA 같은 오픈소스 LLM은 외부 API 활용 능력이 현저히 제한적이다.

- **Gap**: 기존 지시튜닝은 기본 언어 과제에 집중하며 도구 사용 영역을 무시했고, 선행 연구들은 (1) 제한된 API 수와 다양성, (2) 단일 도구 시나리오만 지원, (3) 불충분한 계획 및 추론 능력이라는 문제점을 가지고 있다.

- **Why**: 오픈소스 LLM의 민주화와 커뮤니티 주도 혁신을 위해 다양한 실제 API를 능숙하게 다룰 수 있도록 지원하는 것이 시급하다.

- **Approach**: ChatGPT를 활용한 자동 데이터 구축(API 수집 → 지시생성 → 솔루션 경로 어노테이션), DFSDT 기반 강화된 추론 전략, 신경망 API 리트리버, 그리고 자동 평가기 ToolEval 개발.

## Achievement

![Figure 2](figures/fig2.webp)
*다양한 모델의 도구 사용 평가 결과: Pass Rate와 Win Rate (ChatGPT-ReACT 대비)*

1. **포괄적 데이터셋 구성**: RapidAPI에서 49개 카테고리, 3,451개 도구(Tool), 16,464개 API로 이루어진 ToolBench 구축 (126,486개 지시문, 469,585개 실제 API 호출 포함)

2. **우수한 모델 성능**: ToolLLaMA는 Text-Davinci-003과 Claude-2를 능가하고 ChatGPT와 견줄 만한 성능 달성, GPT-4에만 약간 밀림

3. **다중 도구 처리 능력**: 단일 도구 및 복합 다중 도구 시나리오 모두 처리 가능

4. **강력한 일반화**: 훈련에 미포함된 APIBench 데이터셋에서 Gorilla와 동등한 성능 시연

## How

![Figure 1](figures/fig1.webp)
*ToolBench 구축의 세 단계와 API 리트리버 및 ToolLLaMA 학습 파이프라인*

### 데이터 구축 프로세스

- **API 수집**: RapidAPI Hub에서 10,853개 도구(53,190개 API)를 초기 수집 후, 품질 검증(404 에러, 내부 오류 체크)을 통해 3,451개 도구(16,464개 API) 최종 선정

- **지시문 생성**: ChatGPT를 프롬프팅하여 단일 도구(single-tool), 카테고리 내 다중 도구(intra-category multi-tool), 전체 수집 다중 도구(intra-collection multi-tool) 등 다양한 시나리오의 지시문 자동 생성

- **솔루션 경로 어노테이션**: 깊이 우선 탐색 기반 의사결정 트리(DFSDT) 알고리즘 개발으로 여러 추론 경로 탐색 가능, 실시간 API 호출 결과를 활용한 반복적 재계획 수행

### 핵심 기술 요소

- **DFSDT 알고리즘**: ReACT와 달리 트리 구조로 다중 추론 경로를 체계적으로 탐색하며, 백트래킹(backtrack)을 통해 실패한 경로에서 회피 가능

- **신경망 API 리트리버**: 주어진 지시문에서 16,464개 API 중 관련 API들을 검색하여 추천

- **ToolEval 평가기**: (1) Pass Rate(제한된 예산 내 성공적 실행), (2) Win Rate(솔루션 품질 비교) 두 가지 메트릭으로 자동 평가, ChatGPT 기반으로 높은 인간 평가 상관도 달성

## Originality

- **대규모 실제 API 통합**: 선행 연구 대비 16배 이상 많은 실제 REST API 포함 (16,464 vs. 최대 1,645)

- **다중 도구 시나리오 지원**: 처음으로 단일 도구에 국한되지 않은 복합 다중 도구 작업 지시문 포함

- **DFSDT 알고리즘**: CoT와 ReACT를 능가하는 체계적 트리 기반 탐색 전략의 혁신적 제안

- **자동 데이터 구축 파이프라인**: ChatGPT의 함수 호출(Function Calling) 기능 활용으로 최소 인간 감시로 확장 가능한 구축 프로세스 제시

- **종합 평가 프레임워크**: 자동 평가기 ToolEval 개발로 도구 활용 성능의 일관되고 확장 가능한 평가 가능

## Limitation & Further Study

- **데이터 품질 의존성**: ToolBench 구축의 대부분을 ChatGPT에 의존하므로, 생성된 지시문이나 어노테이션의 잠재적 편향이나 오류가 모델 성능에 영향을 미칠 수 있음

- **API 문서 품질 가정**: 모델이 API 문서만으로 새로운 API를 이해할 수 있다고 가정하지만, 문서가 불충분하거나 모호한 경우 일반화 성능 저하 가능성

- **계산 비용**: 16,464개 API와 126,486개 지시문에 대한 실제 API 호출 및 추론 기반 어노테이션의 높은 계산 비용 미언급

- **평가 메트릭 한계**: Win Rate는 ChatGPT 기반이므로, 사람의 직관과 완전히 일치하지 않을 수 있음

- **후속 연구 방향**:
  - 더 다양한 도메인의 API 통합 (e.g., 대규모 언어 모델 기반 API)
  - 사용자 피드백을 반영한 지속적 모델 개선
  - 멀티모달 API 지원 (이미지, 오디오 등)
  - 실시간 API 변경에 대한 적응 메커니즘

## Evaluation

- **Novelty (혁신성)**: 4.5/5
  - 대규모 실제 API 데이터셋과 다중 도구 시나리오는 선행 연구 대비 명확한 진전이며, DFSDT는 창의적인 알고리즘 기여. 다만 데이터 구축이 ChatGPT에 크게 의존하는 점이 독창성을 약간 제한.

- **Technical Soundness (기술적 타당성)**: 4/5
  - 데이터 구축, 모델 학습, 평가 프레임워크가 모두 체계적이고 논리적. DFSDT의 트리 탐색 방식과 API 리트리버 구현이 타당함. 다만 DFSDT의 계산 복잡도 분석이나 성능 상한선에 대한 이론적 논의 부족.

- **Significance (의의)**: 4.5/5
  - 오픈소스 LLM의 도구 활용 능력 향상에 큰 실질적 기여. ToolBench와 ToolLLaMA가 향후 도구 사용 연구의 벤치마크와 기준 모델 역할 수행할 가능성이 높으며, 공개 코드/모델로 커뮤니티 영향력 극대화.

- **Clarity (명확성)**: 4/5
  - 논문의 구조와 설명이 전반적으로 명확하고, 그림과 표가 효과적으로 개념을 전달. 다만 DFSDT 알고리즘의 의사코드나 상세 동작 원리 설명이 본문에서 다소 부족하고 부록 의존도가 높음.

- **Overall (종합)**: 4.2/5

**총평**: ToolLLM은 오픈소스 LLM의 대규모 실제 API 활용 능력을 체계적으로 확보한 중요한 연구로, 포괄적인 데이터셋, 강화된 추론 알고리즘, 자동 평가 프레임워크를 통해 도구 학습 분야에 실질적 기여를 제시한다. ChatGPT 수준의 성능 달성과 강력한 일반화 능력은 실무 적용 가능성을 높이나, 데이터 구축의 ChatGPT 의존도와 이론적 분석 깊이에서는 개선 여지가 있다.

## Related Papers

- 🔗 후속 연구: [[papers/672_ResearchGym_Evaluating_Language_Model_Agents_on_Real-World_A/review]] — API 도구 사용 능력 평가 방법론을 AI 연구 자동화 평가로 확장한 발전
- 🏛 기반 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — 대규모 도구 사용 평가 프레임워크가 ML 실험 자동화 벤치마크의 기반
- 🔄 다른 접근: [[papers/180_Can_foundation_models_actively_gather_information_in_interac/review]] — 능동적 정보 수집에 중점을 둔 접근과 달리 구체적 API 도구 활용 능력에 집중
- 🏛 기반 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — LLM 도구 사용에 대한 포괄적 서베이에서 제시된 방법론을 대규모 벤치마크로 구현
- 🔗 후속 연구: [[papers/268_Democratizing_AI_scientists_using_ToolUniverse/review]] — 도구 생태계가 더 포괄적인 도구 마스터링으로 확장됩니다.
- 🧪 응용 사례: [[papers/114_Augmented_Language_Models_a_Survey/review]] — 언어모델의 도구 사용 능력 확장 연구가 16000개 이상의 다양한 도구를 마스터하는 대형언어모델 개발에 직접 적용되었다
- 🔗 후속 연구: [[papers/1098_BloClaw_An_Omniscient_Multi-Modal_Agentic_Workspace_for_Next/review]] — BloClaw는 ToolLLM의 16000+ 도구 마스터링 프레임워크를 확장하여 JSON 기반 도구 호출의 취약성을 해결하는 더 견고한 도구 통합 환경을 제공합니다.
- 🔗 후속 연구: [[papers/499_LLM_With_Tools_A_Survey/review]] — 16,000개 이상의 도구를 마스터하는 LLM 훈련으로 도구 활용 능력을 대폭 확장한다.
- 🏛 기반 연구: [[papers/672_ResearchGym_Evaluating_Language_Model_Agents_on_Real-World_A/review]] — 도구 사용 능력을 평가하는 ToolLLM의 방법론을 연구 에이전트 평가로 확장한 기반
- 🔗 후속 연구: [[papers/542_Mlagentbench_Evaluating_language_agents_on_machine_learning/review]] — API 도구 사용 능력 평가를 머신러닝 실험이라는 구체적 도메인으로 특화한 확장
- 🔄 다른 접근: [[papers/180_Can_foundation_models_actively_gather_information_in_interac/review]] — API 도구 사용과 달리 환경과의 능동적 상호작용을 통한 정보 수집 능력에 집중
- 🏛 기반 연구: [[papers/231_Codegen_An_open_large_language_model_for_code_with_multi-tur/review]] — 코드 생성 능력이 API 도구 사용 벤치마크에서 프로그래밍 작업의 기반
