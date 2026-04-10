---
title: "874_WebWatcher_Breaking_New_Frontier_of_Vision-Language_Deep_Res"
authors:
  - "Xinyu Geng"
  - "Peng Xia"
  - "Zhen Zhang"
  - "Xinyu Wang"
  - "Qiuchen Wang"
date: "2025"
doi: "10.48550/arXiv.2508.05748"
arxiv: ""
score: 4.0
essence: "WebWatcher는 비전-언어(Vision-Language, VL) 통합 추론 능력을 갖춘 멀티모달 심층 연구 에이전트로, 합성 멀티모달 궤적(synthetic multimodal trajectories)을 통한 효율적인 학습, 다양한 도구의 활용, 강화학습을 통한 일반화로 웹 검색, 이미지 분석, 웹페이지 탐색 등 복잡한 정보 추구 작업을 수행한다."
tags:
  - "cat/Multi-Agent_Scientific_Discovery_Systems"
  - "sub/Multi-Agent_Language_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Geng et al._2025_WebWatcher Breaking New Frontier of Vision-Language Deep Research Agent.pdf"
---

# WebWatcher: Breaking New Frontier of Vision-Language Deep Research Agent

> **저자**: Xinyu Geng, Peng Xia, Zhen Zhang, Xinyu Wang, Qiuchen Wang | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2508.05748](https://doi.org/10.48550/arXiv.2508.05748)

---

## Essence

![Figure 2](figures/fig2.webp)
*VL 추론 에이전트의 비교: WebWatcher는 순수 시각 추론이나 검색 기반 에이전트를 개별적으로 이길 수 없는 GAIA 사례를 해결하며, 다중 도구 통합과 심층 추론의 강점을 입증*

WebWatcher는 비전-언어(Vision-Language, VL) 통합 추론 능력을 갖춘 멀티모달 심층 연구 에이전트로, 합성 멀티모달 궤적(synthetic multimodal trajectories)을 통한 효율적인 학습, 다양한 도구의 활용, 강화학습을 통한 일반화로 웹 검색, 이미지 분석, 웹페이지 탐색 등 복잡한 정보 추구 작업을 수행한다.

## Motivation

- **Known**: 기존 Deep Research 에이전트(예: GPT-4o, Gemini)들은 텍스트 중심으로 개발되었으며, 텍스트 기반 웹 에이전트들이 BrowseComp, Humanity's Last Exam 같은 고난도 벤치마크에서 인간 수준 이상의 성능을 달성했다.

- **Gap**: 현실 세계의 많은 작업(과학 다이어그램 해석, 그래프 분석, 시각적으로 풍부한 웹 인터페이스 탐색)은 비전과 언어를 통합한 추론이 필수적이지만, 멀티모달 심층 연구는 아직 충분히 탐색되지 않았다. 또한 기존 VL 에이전트들은 OCR, 바운딩박스 추출 등의 시각 도구에만 의존하거나, 검색 에이전트는 검색 도구만 사용하여 복잡한 상호작용 문제 해결에 실패한다.

- **Why**: 높은 난이도의 VL 심층 연구는 (1) 텍스트와 시각 정보 양쪽 모두에서 강한 추론 능력, (2) 웹 검색, 이미지 검색, 웹페이지 방문, 코드 실행 등 다양한 외부 도구의 효과적인 사용이 필요하다.

- **Approach**: (1) 웹 문서 랜덤 워크를 통한 실제 지식 기반 고난도 QA 생성 및 QA-to-VQA 변환 파이프라인으로 고품질 멀티모달 학습 데이터 구성, (2) 도구 사용 행동에 기반한 자동화된 추론 궤적 생성 및 파인튜닝, (3) GRPO 강화학습으로 최적화, (4) BrowseComp-VL 벤치마크 제안으로 평가 개선

## Achievement

![Figure 1](figures/fig1.webp)
*4개 벤치마크에서 WebWatcher의 전체 성능 비교: Humanity's Last Exam-VL에서 13.6점, BrowseComp-VL에서 27.0점, LiveVQA에서 58.7점, MMSearch에서 55.3점으로 GPT-4o, Gemini, Claude 등 폐쇄형 모델과 오픈소스 에이전트들을 능가*

1. **벤치마크 성능 우월성**: 4개의 고난도 VQA 벤치마크(HLE-VL, BrowseComp-VL, LiveVQA, MMSearch)에서 일관되게 기존 오픈소스 에이전트와 폐쇄형 시스템(GPT-4o, Gemini, Claude)을 상회하는 성능 달성(예: BrowseComp-VL에서 27.0점 vs GPT-4o 13.4점)

2. **BrowseComp-VL 벤치마크 구축**: BrowseComp의 복잡성을 시각 도메인으로 확장한 399개 VQA 쌍(Level 1: 199개, Level 2: 200개) 포함 벤치마크 제안으로 멀티모달 에이전트 능력 평가 체계 확립

3. **다중 도구 통합 전략**: 웹 텍스트/이미지 검색, 웹페이지 방문, 코드 실행, OCR 등 5가지 도구를 효과적으로 활용하며, Figure 2의 사례처럼 순수 시각 분석이나 단순 검색 에이전트가 해결 불가능한 문제 해결 입증

## How

![Figure 4](figures/fig4.webp)
*데이터 생성 파이프라인: Level 1과 Level 2의 2단계 프레임워크로 구성되며, QA 생성에서 이미지 검색, 그래프 생성, 검증을 거쳐 최종 VQA 쌍 생성*

### 1. 고품질 학습 데이터 구성

- **QA 기반 생성**: arXiv, GitHub, Wikipedia 등 신뢰할 수 있는 소스에서 루트 URL 수집 → 재귀적 하이퍼링크 순회 → GPT-4o를 통한 다중홉(multi-hop) 추론 QA 쌍 합성
  
- **엔티티 난독화(Entity Obfuscation)**: Level 2에서 구체적인 날짜를 모호한 시간 표현으로, 이름을 마스킹하고 정량 속성을 퍼지(fuzz)하여 컨텍스트 기반 추론 강제

- **QA-to-VQA 변환**: 기존 QA 데이터셋과 호환되는 적응형 변환 파이프라인으로 멀티모달 데이터셋 대규모 확장 가능화

- **다단계 필터링**: 생성된 데이터의 품질과 명확성 확보

### 2. 추론 궤적(Reasoning Trajectory) 자동 생성

- **행동-관찰 기반 구성**: 손으로 작성한 Chain-of-Thought(CoT) 스타일 또는 템플릿 기반 설명 대신, 실제 도구 사용 행동에서 도출된 궤적 생성

- **프롬프팅 + 규칙 기반 필터링**: LLM 기반 프롬프팅과 규칙 기반 필터링 결합으로 고품질 궤적 생성 자동화

- **도구 다양성 반영**: 각 도구의 입출력 형식과 추론 역할의 차이를 반영한 궤적 구성

### 3. 모델 학습 및 최적화

- **파인튜닝**: 합성된 고품질 멀티모달 궤적으로 에이전트 모델 파인튜닝

- **강화학습(GRPO)**: GRPO(Group Relative Policy Optimization) 알고리즘으로 추가 최적화하여 도구 활용 능력 강화

## Originality

- **멀티모달 심층 연구의 개척**: 기존 텍스트 중심 Deep Research 에이전트를 처음으로 멀티모달 도메인으로 확장하며, 단순 시각 도구 의존을 벗어나 텍스트-이미지 통합 추론 체계 구축

- **QA-to-VQA 변환 파이프라인**: 기존 QA 데이터셋의 다중홉 추론 복잡성을 보존하면서 이미지 기반 질문으로 변환하는 획기적인 방법론 제시로, 고품질 멀티모달 학습 데이터 확장성 문제 해결

- **자동화된 도구 기반 궤적 생성**: 템플릿 기반 추론 궤적의 한계를 극복하고 실제 도구 사용 패턴에서 도출된 다양한 궤적 생성으로 모델 일반화 능력 향상

- **BrowseComp-VL 벤치마크**: 멀티모달 에이전트의 고난도 능력을 평가하는 첫 번째 표준화된 벤치마크로, 엔티티 난독화 및 다중 도메인 구성으로 지각(perception)만으로는 해결 불가능한 과제 제시

- **다중 도구 통합 전략**: 웹 검색, 이미지 검색, 웹페이지 탐색, 코드 실행을 유기적으로 조율하는 메커니즘으로, 단일 도구 의존의 한계 극복

## Limitation & Further Study

- **데이터셋 규모의 한계**: BrowseComp-VL의 총 399개 VQA 쌍은 대규모 언어 모델 학습 기준으로 상대적으로 작은 규모이며, 벤치마크 다양성 측면에서 5개 주요 도메인과 17개 세부 분야만 포함. 보다 광범위한 도메인과 대규모 데이터셋으로 확장 필요

- **도구 오류 누적**: 웹 검색 오류, 페이지 로딩 실패, OCR 오류 등 하위 도구의 실패가 최종 답변 정확도에 미치는 영향에 대한 체계적 분석 부족. 오류 전파(error propagation) 메커니즘과 대응 전략 연구 필요

- **비전-언어 모드 간 불균형**: Figure 5의 도구 호출 분석에서 도구 유형별 활용도 편차가 있을 수 있으며, 특정 벤치마크에서 시각 정보의 중요도가 상이할 수 있음을 미처 분석하지 못함

- **실시간 웹 환경 일반화**: 학습 데이터가 특정 시점의 웹 콘텐츠에 기반했을 가능성 높으며, 웹페이지 구조 변화나 최신 정보 반영에 대한 강건성 평가 부재

- **강화학습 수렴 특성**: GRPO 최적화 과정에서 보상 함수 설계, 수렴 속도, 과적합 방지 등의 세부 사항이 명확하지 않아 재현성 저해 우려


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 3.5/5
- Overall: 4/5

**총평**: WebWatcher는 텍스트 중심 web agent를 멀티모달 영역으로 성공적으로 확장한 의미 있는 연구로, 자동화된 데이터 생성 파이프라인과 다중 도구 통합이 핵심 강점이며, BrowseComp-VL

## Related Papers

- 🔄 다른 접근: [[papers/873_WebThinker_Empowering_Large_Reasoning_Models_with_Deep_Resea/review]] — 웹 기반 정보 탐색에서 심층 추론 능력을 강조하는 다른 접근 방식을 제시한다.
- 🔗 후속 연구: [[papers/450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor/review]] — LLM 가이드 웹 브라우징 프레임워크에서 비전-언어 통합으로 확장된 탐색 능력을 보여준다.
- 🏛 기반 연구: [[papers/174_Browsecomp_A_simple_yet_challenging_benchmark_for_browsing_a/review]] — 웹 브라우징의 기본적인 도전 과제를 다루는 벤치마크로 복잡한 웹 탐색의 기초를 제공한다.
