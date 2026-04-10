---
title: "873_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Resea"
authors:
  - "Xiaoxi Li"
  - "Jiajie Jin"
  - "Guanting Dong"
  - "Hongjin Qian"
  - "Yutao Zhu"
date: "2025"
doi: "10.48550/arXiv.2504.21776"
arxiv: ""
score: 4.4
essence: "대규모 추론 모델(LRM)의 정적 지식 의존성을 극복하기 위해, 웹 탐색과 정보 수집을 추론 과정에 통합하는 자율 딥 리서치 에이전트를 제시한다. WebThinker는 LRM이 웹 페이지를 동적으로 탐색하고 실시간으로 보고서를 작성할 수 있도록 지원한다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Search-Augmented_Language_Models"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Li et al._2025_WebThinker Empowering Large Reasoning Models with Deep Research Capability.pdf"
---

# WebThinker: Empowering Large Reasoning Models with Deep Research Capability

> **저자**: Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yutao Zhu | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2504.21776](https://doi.org/10.48550/arXiv.2504.21776)

---

## Essence

![Figure 2](figures/fig2.webp)
*그림 2: RAG 패러다임 비교: (a) 표준 RAG, (b) 사전 정의된 워크플로우가 있는 고급 RAG, (c) WebThinker의 자율적 도구 호출*

대규모 추론 모델(LRM)의 정적 지식 의존성을 극복하기 위해, 웹 탐색과 정보 수집을 추론 과정에 통합하는 자율 딥 리서치 에이전트를 제시한다. WebThinker는 LRM이 웹 페이지를 동적으로 탐색하고 실시간으로 보고서를 작성할 수 있도록 지원한다.

## Motivation

- **Known**: OpenAI-o1, DeepSeek-R1 등의 대규모 추론 모델(LRM)은 뛰어난 장기 추론 능력을 보유하고 있다. 기존 RAG 기법은 사전 정의된 워크플로우를 따르며 전통적 언어 모델(LLM)과 함께 사용된다.

- **Gap**: LRM의 정적 내부 지식은 지식 집약적 작업에서 성능을 제한하며, 다양한 웹 정보를 종합한 포괄적 연구 보고서 생성에 실패한다. 기존 오픈소스 딥 서치 에이전트는 LRM의 깊이 있는 웹 정보 탐색 능력과 검색 엔진과의 긴밀한 상호작용을 제한한다.

- **Why**: 금융, 과학, 공학 등 지식 집약적 분야의 연구자들은 정보 수집에 소요되는 시간과 비용을 단축해야 한다. LRM의 추론 능력과 웹 정보 탐색의 깊이 있는 통합이 실질적 요구사항으로 대두되었다.

- **Approach**: LRM이 추론 과정 중 자율적으로 웹 검색, 페이지 네비게이션, 실시간 보고서 작성을 수행하도록 하는 WebThinker를 제안한다. Deep Web Explorer 모듈과 Autonomous Think-Search-and-Draft 전략, 그리고 RL 기반 DPO 훈련을 결합한다.

## Achievement

![Figure 1](figures/fig1.webp)
*그림 1: 두 가지 작업에서 WebThinker와 다른 모델의 전체 성능 비교: 복잡한 문제 해결(좌측)과 과학 보고서 생성(우측)*

1. **복잡한 추론 벤치마크 성능**: GPQA(64.6%), GAIA(48.5%), WebWalkerQA(46.5%), HLE(15.8%)에서 강력한 결과를 달성. Search-o1-32B 대비 GAIA에서 21.9%, HLE에서 36.2% 우월.

2. **과학 보고서 생성**: Glaive 데이터셋에서 Grok3 DeeperSearch, Gemini 2.0 Deep Research를 능가. 종합성(Comprehensive) 8.3, 철저성(Thorough) 8.4, 사실성(Factuality) 7.7 달성.

3. **스케일링 효율성**: DeepSeek-R1 기반 모델에서 7B부터 32B까지 일관된 성능 향상 입증.

## How

![Figure 3](figures/fig3.webp)
*그림 3: WebThinker 프레임워크 개요. (1) 문제 해결 모드는 Deep Web Explorer로 웹 탐색을 가능하게 하고, (2) 보고서 생성 모드는 사고-검색-작성을 동시에 수행*

### 문제 해결 모드 (Problem-Solving Mode)

- **Deep Web Explorer 모듈**: LRM이 지식 격차 마주칠 때 자율적으로 웹 검색 개시
- **페이지 네비게이션**: 링크/버튼 클릭을 통한 동적 웹 페이지 탐색
- **정보 추출**: 관련 정보를 수집하여 추론 계속
- **순차적 탐색**: 현재 검색 결과 기반으로 후속 검색 및 깊은 링크 순회

### 보고서 생성 모드 (Report Generation Mode)

- **Autonomous Think-Search-and-Draft 전략**: 보고서 전체 생성 후 검색이 아닌, 실시간 사고와 검색 중 작성
- **3가지 전문화 도구**:
  - 특정 장(章)의 콘텐츠 작성(Write)
  - 현재 보고서 검토(Check)
  - 보고서 편집(Edit)
- **Document Memory**: 탐색한 웹 페이지를 누적하여 사실 기반 보고서 작성 지원
- **조화로운 통합**: 신규 발견 정보에 적응하면서 종합성, 일관성 유지

### 훈련 전략

- **RL 기반 DPO**: 복잡 작업에서 대규모 추론 궤적(trajectory) 샘플링
- **온라인 DPO**: 추론 정확성, 도구 사용, 최종 출력 기반 선호도 쌍 구성
- **반복적 개선**: 모델의 인지, 추론, 연구 도구 상호작용 능력을 점진적으로 향상

### 형식화

- 방정식 (1): 도구를 활용한 추론과 최종 출력 생성의 결합 확률
- 방정식 (2): Deep Web Explorer를 호출하는 문제 해결 과정의 형식화

## Originality

- **LRM과 웹 탐색의 깊이 있는 통합**: 기존 RAG가 사전 정의된 워크플로우를 따르는 반면, WebThinker는 LRM의 연속적 사고 과정 내에서 도구 호출을 자율적으로 수행. 이는 LRM의 추론 능력을 온전히 활용하는 근본적으로 다른 접근.

- **동시적 Think-Search-and-Draft 전략**: 검색 완료 후 보고서 작성이 아닌, 사고와 검색 중에 실시간으로 작성하는 전략은 저자들의 독창적 기여. Document Memory를 통해 사실성 확보.

- **RL 기반 온라인 DPO 훈련**: 도구 사용까지 포함한 end-to-end 최적화. 기존 감독 학습이나 오프라인 RL이 아닌 온라인 DPO를 통한 반복적 개선 방식.

- **종합적 벤치마크 평가**: GPQA, GAIA, WebWalkerQA, HLE, Glaive 등 다양한 복잡 추론 및 보고서 생성 작업에 대한 광범위한 평가. 기존 방법과 최신 proprietary 시스템(Grok3, Gemini 2.0) 대비.

## Limitation & Further Study

- **웹 검색의 신뢰성**: 검색 결과의 정확성과 최신성에 의존하는 문제. 잘못된 정보나 오래된 정보가 포함될 경우 모델의 성능 저하 가능성.

- **계산 비용**: 웹 탐색, 페이지 크롤링, 추가 LLM 호출로 인한 높은 계산 오버헤드. 실시간 애플리케이션에서의 지연 시간 영향.

- **Document Memory의 확장성**: 장시간 탐색 시 Document Memory의 크기와 검색 효율성 문제. 매우 많은 웹 페이지 처리 시의 성능 열화 우려.

- **도구 호출 오버헤드**: LRM의 과도한 도구 호출로 인한 비효율성. 언제 검색을 멈출지의 판단 기준 명확화 필요.

- **다언어 및 도메인 특화**: 현재 주로 영어와 특정 도메인에 중점. 다양한 언어와 특수 도메인(의료, 법률 등)에 대한 확장 연구 필요.

- **후속 연구 방향**:
  - 웹 정보의 신뢰도 검증 메커니즘 강화
  - 도구 호출 최소화를 위한 효율적 탐색 알고리즘
  - 멀티모달 정보 처리 (이미지, 표, 차트 등)
  - 동적 지식 업데이트 메커니즘


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4.5/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 4.4/5

**총평**: WebThinker는 LRM의 추론 능력과 웹 정보 탐색을 효과적으로 결합하여 복잡한 지식 집약적 작업에서 뛰어난 성과를 보여준다. 특히 온라인 DPO 기반의 end-to-end 최적화와 실시간 Think-Search-and-Draft 전략은 고도로 독창적이며, 광범위한 벤치마크에서 proprietary 시스템을 능가하는 실증적 성과는 중요하다. 다만 계산 비용과 웹 신뢰성 문제는 실제 배포 시 고려해야 할 과제이다.

## Related Papers

- 🔄 다른 접근: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — 두 논문 모두 추론 과정에서의 검색 통합을 다루되 WebThinker는 웹 탐색, Search-R1은 검색 엔진 활용에 특화되어 있다.
- 🔗 후속 연구: [[papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/review]] — ReSearch의 강화학습 기반 검색 학습은 WebThinker의 웹 탐색 능력을 더욱 체계적이고 자동화된 방식으로 발전시킨다.
- 🧪 응용 사례: [[papers/592_Openreviewer_A_specialized_large_language_model_for_generati/review]] — WebThinker의 동적 웹 탐색 능력은 OpenReviewer의 과학 문헌 생성 작업에서 실시간 정보 수집을 통해 더 정확한 리뷰를 생성할 수 있다.
- 🔗 후속 연구: [[papers/740_Search-R1_Training_LLMs_to_Reason_and_Leverage_Search_Engine/review]] — WebThinker의 웹 탐색 능력은 Search-R1의 검색 엔진 활용을 더 동적이고 상호작용적인 정보 수집으로 발전시킨다.
- 🏛 기반 연구: [[papers/667_ReSearch_Learning_to_Reason_with_Search_for_LLMs_via_Reinfor/review]] — WebThinker의 웹 탐색과 정보 수집 통합은 ReSearch의 검색 쿼리와 추론 체인 생성에 더 동적인 정보 수집 방법론을 제공한다.
- 🔄 다른 접근: [[papers/874_WebWatcher_Breaking_New_Frontier_of_Vision-Language_Deep_Res/review]] — 웹 기반 정보 탐색에서 심층 추론 능력을 강조하는 다른 접근 방식을 제시한다.
