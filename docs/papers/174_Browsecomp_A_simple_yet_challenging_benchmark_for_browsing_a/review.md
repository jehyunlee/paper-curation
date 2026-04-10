---
title: "174_Browsecomp_A_simple_yet_challenging_benchmark_for_browsing_a"
authors:
  - "J. Wei"
  - "Zhiqing Sun"
  - "Spencer Papay"
  - "Steve McKinney"
  - "Jeffrey S. Han"
date: "2025"
doi: "N/A"
arxiv: ""
score: 4.5
essence: "웹 에이전트의 능력을 평가하기 위해 1,266개의 어려운 질문으로 구성된 BrowseComp 벤치마크를 제시한다. 이 벤치마크는 깊이 있는 웹 탐색과 창의적인 검색 능력을 요구하면서도 답변이 짧고 검증이 용이한 특징을 갖는다."
tags:
  - "cat/Scientific_Document_Analysis_and_Retrieval"
  - "sub/Scholarly_Document_QA"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wei et al._2025_Browsecomp A simple yet challenging benchmark for browsing agents.pdf"
---

# BrowseComp: A simple yet challenging benchmark for browsing agents

> **저자**: J. Wei, Zhiqing Sun, Spencer Papay, Steve McKinney, Jeffrey S. Han, Isa Fulford, Hyung Won Chung, Alex Tachard Passos, William Fedus, Amelia Glaese | **날짜**: 2025 | **DOI**: N/A

---

## Essence

![Figure 1](figures/fig1.webp) *Figure 1: 테스트 시 계산량(browsing effort)에 따른 OpenAI Deep Research의 BrowseComp 성능. 정확도가 계산량에 비례하여 증가*

웹 에이전트의 능력을 평가하기 위해 1,266개의 어려운 질문으로 구성된 BrowseComp 벤치마크를 제시한다. 이 벤치마크는 깊이 있는 웹 탐색과 창의적인 검색 능력을 요구하면서도 답변이 짧고 검증이 용이한 특징을 갖는다.

## Motivation

- **Known**: 기존 정보 검색(Information Retrieval) 벤치마크들(QUAC, SQuAD, HotpotQA 등)은 최근 언어 모델의 발전으로 포화되었으며, 쉽게 찾을 수 있는 정보 검색에 초점을 맞추고 있음
- **Gap**: 실제 웹 에이전트가 필요한 '어려운 정보 탐색', 특히 여러 웹페이지에 걸친 복잡한 조건을 만족하는 정보 찾기 능력을 평가할 수 있는 벤치마크 부재
- **Why**: 챗봇에서 추론 모델(reasoner), 에이전트로 진화하는 AI 시스템에서 지속적인 웹 탐색 능력이 점점 중요해지고 있음
- **Approach**: 인간 트레이너가 수동으로 10분 이내에 단순 구글 검색으로는 풀 수 없고, 기존 모델(GPT-4o, Claude 등)도 풀지 못하는 1,266개의 질문과 짧은 답변을 수집하여 벤치마크 구성

## Achievement

![Figure 2](figures/fig2.webp) *Figure 2: BrowseComp의 주제 분포. TV/영화(16.2%), 과학기술(13.7%), 미술(10.0%) 등 다양한 영역 커버*

1. **벤치마크 품질 검증**: 인간 트레이너가 1,255개 문제 중 367개(29.2%)만 2시간 내 해결 가능하며, 이 중 86.4%가 참조 답변과 일치—벤치마크의 높은 난이도 입증

2. **포괄적 평가 커버리지**: 10개 카테고리(TV/영화, 과학기술, 미술, 역사, 스포츠, 음악 등) 1,266개 문제로 다양한 도메인의 지식 검색 능력 측정

3. **스케일 가능한 성능 곡선**: OpenAI Deep Research가 테스트 시 계산량 증가에 따라 부드러운 성능 향상을 보여 모델 개선을 정량화할 수 있는 감도 있는 벤치마크임을 입증

## How

![Figure 3](figures/fig3.webp) *Figure 3: 인간이 문제를 해결한 시간 분포(좌)와 포기한 시간 분포(우). 해결된 문제는 1시간부터 3시간까지 분산, 포기된 경우 대부분 2시간 근처*

**데이터 수집 및 검증 방법론:**

- **역제곱 방식(Inverted Question Design)**: 실제 사실에서 시작하여 검증은 쉽지만 발견은 어려운 질문으로 변환. 예) 특정 학회에서 특정 대학 출신 특정 저자로 논문 찾기
  
- **난이도 검증 3단계**:
  1. 기존 모델(GPT-4o, o1, Deep Research 초기 버전) 불가능 확인
  2. 5회 단순 구글 검색으로 첫 페이지에서 답 찾기 불가능 확인
  3. 다른 인간 트레이너가 2시간 내 40% 이상 해결 불가능할 때까지 개선
  
- **단순성과 검증 용이성**: 모든 답변을 단일 짧은 텍스트 문자열로 제한하고, GPT 기반 의미적 동등성(semantic equivalence) 검사자를 사용한 자동 평가

- **위음성(False Negative) 완화**: 검증 불가능한 추가 정답 존재 가능성에 대비하여, 트레이너가 창의적 제약 추가 및 다른 트레이너의 검증 피드백을 통해 문제 정제

## Originality

- **프로그래밍 경진대회 유추 적용**: CodeForces/LeetCode가 코딩 능력의 핵심 지표인 것처럼, BrowseComp를 웹 탐색의 핵심 능력(지속성, 창의성, 팩트 추론)을 측정하는 유사한 패러다임으로 정위

- **역제곱 데이터 생성 철학**: 기존 QA 벤치마크(SimpleQA를 따름)와 달리, 검증 용이성과 발견 난이도를 명시적으로 분리하여 에이전트의 진정한 탐색 역량을 측정

- **인간 기준선의 투명한 공개**: 트레이너 성능(29.2% 해결률, 평균 2시간 소요)을 명확히 제시하여 모델 성능 해석의 맥락 제공

## Limitation & Further Study

- **제한된 평가 범위**: 실제 사용자 쿼리 분포를 반영하지 못하며, 긴 답변 생성, 질의의 모호성 해결, 대화형 명확화 등 실전 에이전트 필수 능력 미포함

- **단일 정답 가정**: 역제곱 설계의 특성상 참조 답변 외 추가 정답 존재 가능성을 완전히 배제할 수 없어, 이중 채점 자동화의 한계 존재

- **도메인 편향 위험**: 트레이너의 개인적 관심사 기반 질문 생성으로 인한 주제 분포 편향 가능성(TV/영화 16.2%로 과다 대표)

- **후속 연구 방향**:
  - 경진대회 수준의 웹 탐색 능력을 가진 전문가(탐정, 조사 기자)의 성능 분석
  - 병렬 샘플링(parallel sampling)과 신뢰도 기반 조기 종료 메커니즘의 효율성 연구
  - 장문 답변, 불확실성 처리 등을 포함한 확장 벤치마크 개발

## Evaluation

- **Novelty**: 4/5 — 웹 에이전트용 벤치마크 자체는 새롭고, 역제곱 설계 철학이 창의적이나, 기본 QA 평가 프레임워크는 기존 연구(SimpleQA)를 따름

- **Technical Soundness**: 4/5 — 데이터 수집 검증 프로토콜이 철저하고 인간 기준선이 명확하나, 의미적 동등성 판정자의 오류율과 추가 정답 존재 가능성에 대한 정량적 분석 부족

- **Significance**: 5/5 — 빠르게 성장하는 웹 에이전트 연구에 명확한 표준 벤치마크 제공, OpenAI Deep Research 개발에 직접 활용되는 실용성 높음

- **Clarity**: 5/5 — 문제 설명, 데이터 특성, 평가 방법론이 매우 명확하고 구체적 사례를 풍부히 제시

- **Overall**: 4.5/5

**총평**: BrowseComp는 급성장하는 웹 에이전트 분야에 명확한 표준을 제공하는 실용적이고 잘 설계된 벤치마크이지만, 실제 사용자 요구(긴 답변, 모호성 해결)를 포함한 확장이 향후 필요하다.

## Related Papers

- 🔄 다른 접근: [[papers/793_The_Adoption_and_Usage_of_AI_Agents_Early_Evidence_from_Perp/review]] — 웹 에이전트 평가를 위한 벤치마크로서 AI 에이전트 사용 패턴 연구와 상호 보완적인 평가 관점을 제시합니다.
- 🏛 기반 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 도구 사용을 학습하는 언어모델 연구의 기반 위에서 더 복잡한 웹 브라우징 능력을 평가하는 벤치마크를 구축합니다.
- 🔗 후속 연구: [[papers/450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor/review]] — LLM 가이드 브라우징 프레임워크의 성능을 체계적으로 평가할 수 있는 도전적인 벤치마크를 제공합니다.
- 🏛 기반 연구: [[papers/874_WebWatcher_Breaking_New_Frontier_of_Vision-Language_Deep_Res/review]] — 웹 브라우징의 기본적인 도전 과제를 다루는 벤치마크로 복잡한 웹 탐색의 기초를 제공한다.
- 🧪 응용 사례: [[papers/793_The_Adoption_and_Usage_of_AI_Agents_Early_Evidence_from_Perp/review]] — AI 에이전트 사용 패턴 연구의 실제 평가를 위한 도전적인 웹 브라우징 벤치마크를 제공합니다.
- 🏛 기반 연구: [[papers/813_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools/review]] — 언어모델의 도구 사용 학습 연구가 복잡한 웹 브라우징 에이전트 평가 벤치마크의 기술적 기반을 제공합니다.
- 🔗 후속 연구: [[papers/450_Knowledge_navigator_Llm-guided_browsing_framework_for_explor/review]] — 단순한 브라우징 과제를 대규모 과학 문헌의 체계적 탐색으로 확장한 고도화된 시스템입니다.
