---
title: "872_Webdancer_Towards_autonomous_information_seeking_agency"
authors:
  - "Jing Wu"
  - "Baixuan Li"
  - "Runnan Fang"
  - "Weihua Yin"
  - "Liwen Zhang"
date: "2025"
doi: "10.48550/arXiv.2505.22648"
arxiv: ""
score: 3.0
essence: "본 논문은 웹 환경에서 자율적 정보 탐색을 수행하는 에이전트(WebDancer)를 구축하기 위한 체계적 파이프라인을 제시한다. 데이터 중심의 관점에서 고품질 탐색 데이터와 궤적(trajectory)을 생성하고, 감독학습(SFT)과 강화학습(RL)을 순차적으로 적용하여 멀티스텝 정보 탐색 능력을 갖춘 에이전트를 학습시킨다."
tags:
  - "cat/Reinforcement_Learning_and_Self-Verification"
  - "sub/Autonomous_Agent_Learning_Systems"
  - "topic/ai4s"
pdf: "C:/Users/jehyu/GoogleDrive/Zotero/Wu et al._2025_Webdancer Towards autonomous information seeking agency.pdf"
---

# Webdancer: Towards autonomous information seeking agency

> **저자**: Jing Wu, Baixuan Li, Runnan Fang, Weihua Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Xi Zhang, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou | **날짜**: 2025 | **DOI**: [10.48550/arXiv.2505.22648](https://doi.org/10.48550/arXiv.2505.22648)

---

## Essence

![Figure 1](figures/fig1.webp)
*그림 1: CRAWLQA와 E2HQA 두 가지 웹 데이터 생성 파이프라인. CRAWLQA는 웹 페이지 크롤링을 통해 깊이 있는 질문을 구성하고, E2HQA는 간단한 질문을 반복적으로 복잡하게 변환하여 멀티스텝 추론을 요구하는 QA 쌍을 생성한다.*

본 논문은 웹 환경에서 자율적 정보 탐색을 수행하는 에이전트(WebDancer)를 구축하기 위한 체계적 파이프라인을 제시한다. 데이터 중심의 관점에서 고품질 탐색 데이터와 궤적(trajectory)을 생성하고, 감독학습(SFT)과 강화학습(RL)을 순차적으로 적용하여 멀티스텝 정보 탐색 능력을 갖춘 에이전트를 학습시킨다.

## Motivation

- **Known**: ChatGPT Deep Research, Grok DeepSearch 등 최근 에이전트 시스템이 강력한 정보 탐색 능력을 보여주고 있으며, 기존 방법들은 프롬프트 엔지니어링 또는 감독학습/강화학습을 통해 탐색 능력을 부여해왔다.

- **Gap**: 기존 데이터셋(2WikiQA, GAIA 등)은 얕은 쿼리(2-3단계)만 포함하며, 웹 에이전트 학습을 위한 충분한 규모의 복잡한 질문 데이터셋이 부족하다. 또한 현재의 SFT/RL 패러다임은 정보 탐색 행동의 잠재력을 충분히 활용하지 못하고 있다.

- **Why**: 실제 세계의 복잡한 문제 해결을 위해서는 (1) 사용자 의도와 상호작용 맥락을 반영한 고품질 탐색 데이터, (2) 장기 추론과 작업 분해를 지원하는 신뢰할 수 있는 궤적, (3) 분포 외(out-of-distribution) 환경에서도 일반화 가능한 학습 전략이 필요하다.

- **Approach**: 데이터 중심의 관점에서 CRAWLQA(웹 크롤링 기반)와 E2HQA(점진적 난이도 상향)를 통해 멀티스텝 QA 쌍을 대규모로 생성하고, 거절 샘플링(rejection sampling)을 통해 LLM과 LRM(Large Reasoning Model)으로부터 고품질 궤적을 수집한 후, RFT(거절 샘플링 미세조정)와 DAPO(동적 샘플링 정책 최적화) RL을 순차 적용한다.

## Achievement

![Figure 2](figures/fig2.webp)
*그림 2: 제안된 훈련 프레임워크 개요. SFT 단계에서는 재포맷된 궤적으로 콜드 스타트를 수행하고, RL 단계에서는 DAPO 알고리즘으로 에이전트의 의사결정과 일반화 능력을 최적화한다.*

![Figure 4](figures/fig4.webp)
*그림 4: GAIA 벤치마크에서 Pass@1, Pass@3, Cons@3 지표를 사용한 상세한 평가 결과. WebDancer는 강력한 성능을 달성한다.*

1. **멀티스텝 정보 탐색 데이터셋 구축**: CRAWLQA와 E2HQA를 통해 기존 데이터셋보다 깊이 있는 멀티홉 추론을 요구하는 QA 쌍을 대규모로 생성. CRAWLQA는 실제 웹 환경의 구조를 반영하고, E2HQA는 단순 질문을 점진적으로 복잡화하여 약에서 강 에이전트로의 학습 경로를 제공.

2. **체계적 훈련 파이프라인의 효과성**: GAIA와 WebWalkerQA 벤치마크에서 강력한 성능 달성. 데이터 효율성 분석을 통해 제안된 방법의 우월성을 입증하였으며, RL 단계에서의 DAPO 알고리즘이 SFT 단계에서 미활용된 QA 쌍을 효과적으로 활용.

3. **에이전트 학습에 대한 체계적 분석**: 짧은 CoT(Short-CoT)와 긴 CoT(Long-CoT)의 역할, 거절 샘플링의 효과, RL 알고리즘의 영향 등에 대한 상세한 분석을 제시하여 향후 에이전트 개발을 위한 실행 가능한 지침 제공.

## How

![Figure 1](figures/fig1.webp)

### 1단계: 심층 정보 탐색 데이터셋 합성

**CRAWLQA**
- 공식 및 신뢰성 있는 웹사이트(arXiv, GitHub, Wiki 등)의 루트 URL 수집
- 하이퍼링크를 따라 서브페이지를 재귀적으로 탐색하여 인간의 웹 탐색 행동 모방
- GPT-4o를 사용하여 수집된 콘텐츠에서 COUNT, MULTI-HOP, INTERSECTION 등 설계된 유형의 질문 생성

**E2HQA**
- SimpleQA 스타일의 기본 QA 쌍에서 시작
- 각 반복에서 엔티티를 추출 → 검색 엔진으로 관련 정보 수집 → LLM으로 새로운 질문 생성
- 수식: $R_n = \pi(S(C_n))$ (여기서 $\pi$는 LLM, $S$는 검색 엔진)
- 반복 횟수를 조절하여 난이도를 체계적으로 증가

### 2단계: 에이전트 궤적 거절 샘플링

**ReAct 기반 에이전트 설정**
- 궤적 구조: Thought(τ) - Action(α) - Observation(o) 라운드의 반복
- Action 공간: search(쿼리, 필터_년도), visit(목표, URL) 두 가지 웹 상호작용 도구
- 관찰값: search 액션은 상위 10개 제목/스니펫, visit 액션은 요약 모델 $M_s$로 생성된 증거/요약

**Short CoT & Long CoT 구성**
- Short CoT: GPT-4o를 이용한 직접 궤적 수집
- Long CoT: LRM(QwQ-Plus)에 역사적 액션과 관찰을 순차적으로 제공하여 자율적 다음 액션 결정
  - LRM의 중간 추론 과정("<reasoning_content>")을 감독 신호로 보존

### 3단계: 감독 미세조정(SFT)을 통한 콜드 스타트

- 거절 샘플링으로 수집된 고품질 궤적을 포맷 지시사항 따르기에서 에이전트 작업으로 적응
- Short CoT와 Long CoT 궤적을 함께 활용하여 다양한 추론 패턴 학습

### 4단계: 강화학습(RL)을 통한 일반화 향상

- **DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization)** 알고리즘 적용
- 동적 샘플링 메커니즘으로 SFT 단계에서 미활용된 QA 쌍을 효과적으로 활용
- 에이전트의 의사결정 최적화 및 분포 외 웹 환경에서의 견고성 강화

## Originality

- **데이터 합성의 이원적 접근**: CRAWLQA(웹 구조 기반)와 E2HQA(점진적 복잡화)를 조합하여 기존의 단순한 필터링 기반 어려운 QA 쌍 구성과 달리, 체계적으로 멀티스텝 탐색을 요구하는 데이터를 대규모로 생성하는 방법론의 혁신성.

- **LRM(Large Reasoning Model) 활용의 신규성**: Long CoT 생성을 위해 QwQ-Plus와 같은 추론 모델을 처음으로 에이전트 궤적 생성에 활용하여, 복잡한 추론 패턴을 에이전트가 학습할 수 있도록 함.

- **체계적 훈련 파이프라인**: 기존 연구들이 SFT 또는 RL 중 하나만 강조한 것과 달리, RFT(거절 샘플링 미세조정) → DAPO RL의 순차적 2단계 접근법으로 콜드 스타트 효율성과 일반화 성능을 동시에 달성.

- **포괄적인 분석 프레임워크**: 데이터 효율성, 에이전트 시스템 평가, 에이전트 학습에 대한 상세한 분석을 통해 향후 에이전트 개발을 위한 실행 가능한 인사이트 제공.

## Limitation & Further Study

- **데이터 합성의 자동화 품질**: CRAWLQA와 E2HQA 모두 GPT-4o에 의존하고 있으므로, 생성된 질문의 다양성과 품질이 프롬프트 설계에 크게 의존할 가능성. 자동 합성된 데이터의 검증 메커니즘에 대한 상세한 논의 부족.

- **웹 환경 복잡성의 제한**: 실험은 GAIA, WebWalkerQA 등 정적 벤치마크에서만 평가되었으며, 동적으로 변화하는 실제 웹 환경(로그인 필요, JavaScript 렌더링 등)에서의 성능은 미평가.

- **행동 공간의 단순화**: 검색(search)과 방문(visit) 두 가지 액션만 고려하여, 스크롤, 폼 입력 등 더 복잡한 웹 상호작용은 미포함. 다양한 도구의 조합이 성능에 미치는 영향 분석 필요.

- **계산 비용의 투명성 부족**: LRM 사용, DAPO RL 훈련 등의 계산 비용이 명시되지 않아, 실제 배포 가능성 평가 어려움.

- **향후 연구 방향**: (1) 멀티모달 웹 이해(이미지, 비디오 등) 통합, (2) 온라인 강화학습으로의 확장, (3) 사용자 피드백 기반 적응형 에이전트 개발, (4) 다국어 웹 탐색 능력 강화.


## Evaluation

- Novelty: 4.5/5
- Technical Soundness: 4/5
- Significance: 4.5/5
- Clarity: 4/5
- Overall: 3/5

## Related Papers

- 🔄 다른 접근: [[papers/447_Iterative_self-incentivization_empowers_large_language_model/review]] — 두 논문 모두 웹 기반 에이전트를 다루되 WebDancer는 정보 탐색, EXSEARCH는 자기-인센티브화 기반 검색에 특화되어 있다.
- 🔗 후속 연구: [[papers/871_WebAgent-R1_Training_Web_Agents_via_End-to-End_Multi-Turn_Re/review]] — WebAgent-R1의 종단 간 다중턴 강화학습은 WebDancer의 감독학습-강화학습 순차 파이프라인을 더 통합적인 학습 프레임워크로 발전시킨다.
- 🧪 응용 사례: [[papers/888_X-webagentbench_A_multilingual_interactive_web_benchmark_for/review]] — X-WebAgentBench의 다국어 웹 벤치마크는 WebDancer의 자율적 정보 탐색 에이전트를 다양한 언어와 문화적 맥락에서 평가하고 개선할 수 있다.
- 🔄 다른 접근: [[papers/447_Iterative_self-incentivization_empowers_large_language_model/review]] — 두 논문 모두 정보 검색 에이전트를 다루되 EXSEARCH는 자기-인센티브화, WebDancer는 감독학습과 강화학습 순차 적용에 초점을 맞춘다.
